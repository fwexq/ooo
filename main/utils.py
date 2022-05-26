from main.models.post.models import Post



class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        post = Post.objects.all()
        return context