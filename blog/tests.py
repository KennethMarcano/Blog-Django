from django.test import TestCase
from django.urls import reverse
from .models import Post, Comment

class PostListTest(TestCase):
    def setUp(self):
        self.post1 = Post.objects.create(title='Test', body='Corpo do test')
        self.post2 = Post.objects.create(title='Test-2', body='Corpo do test-2')
    
    def test_render_template_correct(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_list.html')

    def test_context_include_posts(self):
        response = self.client.get(reverse('post_list'))
        self.assertIn('posts', response.context)
        self.assertEqual(len(response.context['posts']), 2)
        self.assertEqual(response.context['posts'][0], self.post1)
    
    def test_add_valid_form_post(self):
        response = self.client.post(reverse('post_list'), {
            'title': 'Post Novo',
            'body': 'Corpo Novo',
            'post_form': 'submit',
        })
        self.assertEqual(response.status_code, 302)
        posts = Post.objects.all()
        self.assertEqual(len(posts), 3)
        self.assertEqual(posts[2].title, 'Post Novo')
    
    def test_add_invalid_form_post(self):
        response = self.client.post(reverse('post_list'), {
            'title': '',
            'body': 'Corpo Novo',
            'post_form': 'submit',
        })
        self.assertEqual(response.status_code, 200)
        posts = Post.objects.all()
        self.assertEqual(len(posts), 2)
    
    def test_delete_post(self):
        response = self.client.post(reverse('post_delete', args=[self.post1.id]))
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('post_list'))
        self.assertIn('posts', response.context)
        self.assertEqual(len(response.context['posts']), 1)

class PostDetailTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(title='Test', body='Corpo do test')
        self.comment1 = Comment.objects.create(post=self.post, author='Python3', text='Texto do comentario')
        self.comment2 = Comment.objects.create(post=self.post, author='Kenneth', text='Texto do comentario 2')
    
    def test_render_template_correct(self):
        response = self.client.get(reverse('post_detail', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_detail.html')

    def test_context_include_post_with_comments(self):
        response = self.client.get(reverse('post_detail', args=[self.post.id]))
        self.assertIn('post', response.context)
        self.assertEqual(response.context['post'].comments.count(), 2)
        self.assertEqual(response.context['post'].comments.first(), self.comment1)

    def test_add_valid_form_comment(self):
        self.assertEqual(self.post.comments.count(), 2)
        response = self.client.post(reverse('post_detail', args=[self.post.id]), {
            'author': 'Comentario Novo',
            'text': 'Texto do comentario Novo',
        })
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('post_detail', args=[self.post.id]))
        self.assertEqual(response.context['post'].comments.count(), 3)
        self.assertEqual(response.context['post'].comments.last().author, 'Comentario Novo')

    def test_add_invalid_form_comment(self):
        self.assertEqual(self.post.comments.count(), 2)
        response = self.client.post(reverse('post_detail', args=[self.post.id]), {
            'author': '',
            'text': 'Texto do comentario Novo',
        })
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('post_detail', args=[self.post.id]))
        self.assertEqual(response.context['post'].comments.count(), 2)
    
    def test_delete_comment(self):
        response = self.client.post(reverse('comment_delete', args=[self.post.id, self.comment1.id]))
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('post_detail', args=[self.post.id]))
        self.assertEqual(response.context['post'].comments.count(), 1)

class PostEditTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(title='Test', body='Corpo do test')
    
    def test_render_template_correct(self):
        response = self.client.get(reverse('post_edit', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_edit.html')

    def test_context_include_post(self):
        response = self.client.get(reverse('post_edit', args=[self.post.id]))
        self.assertIn('post', response.context)
        self.assertEqual(response.context['post'].title, 'Test')
        self.assertEqual(response.context['post'].body, 'Corpo do test')

    def test_edit_valid_post(self):
        response = self.client.post(reverse('post_edit', args=[self.post.id]), {
            'title': 'Test editado',
            'body': 'Corpo Editado',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.first().title, 'Test editado')
        self.assertEqual(Post.objects.first().body, 'Corpo Editado')
    
    def test_edit_invalid_post(self):
        response = self.client.post(reverse('post_edit', args=[self.post.id]), {
            'title': '',
            'body': 'Corpo Editado',
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Post.objects.first().title, 'Test')
        self.assertEqual(Post.objects.first().body, 'Corpo do test')

class CommentEditTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(title='Test', body='Corpo do test')
        self.comment = Comment.objects.create(post=self.post, author='Python3', text='Texto do comentario')
    
    def test_render_template_correct(self):
        response = self.client.get(reverse('comment_edit', args=[self.post.id, self.comment.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/comment_edit.html')

    def test_context_include_comment(self):
        response = self.client.get(reverse('comment_edit', args=[self.post.id, self.comment.id]))
        self.assertIn('comment', response.context)
        self.assertEqual(response.context['comment'].author, 'Python3')
        self.assertEqual(response.context['comment'].text, 'Texto do comentario')

    def test_edit_valid_comment(self):
        response = self.client.post(reverse('comment_edit', args=[self.post.id, self.comment.id]), {
            'author': 'Author editado',
            'text': 'Text Editado',
        })
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('comment_edit', args=[self.post.id, self.comment.id]))
        self.assertEqual(response.context['comment'].author, 'Author editado')
        self.assertEqual(response.context['comment'].text, 'Text Editado')
    
    def test_edit_invalid_comment(self):
        response = self.client.post(reverse('comment_edit', args=[self.post.id, self.comment.id]), {
            'author': '',
            'text': 'Text Editado',
        })
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('comment_edit', args=[self.post.id, self.comment.id]))
        self.assertEqual(response.context['comment'].author, 'Python3')
        self.assertEqual(response.context['comment'].text, 'Texto do comentario')