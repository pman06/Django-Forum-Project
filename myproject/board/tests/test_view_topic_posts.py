from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse, resolve

from ..models import Board, Post, Topic
from ..views import topic_posts


class TopicPostsTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='john', email = 'john@mail.com', password='123abcdef')
        board = Board.objects.create(name='Django', description='Django Board')
        topic = Topic.objects.create(subject='Test Subjects', board=board, starter = user)
        Post.objects.create(message='Lorem ipsum dolor sit amet', topic=topic, created_by=user)
        url = reverse('topic_posts', kwargs={'pk':board.pk, 'topic_pk':topic.pk})
        self.response = self.client.get(url)

    def status_code(self):
        self.assertEqual(self.status_code, 200)

    def test_view_functon(self):
        view = resolve('/boards/1/topics/1')
        self.assertEqual(view.func, topic_posts)
