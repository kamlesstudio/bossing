from django.utils import timezone
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


from bossing_up.models import BlackBusiness

class Comment(models.Model):
	post = models.ForeignKey(BlackBusiness, on_delete=models.CASCADE, related_name='comments')
	author = models.CharField(max_length=200)
	email = models.EmailField(max_length=80, null=True, blank=True)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	approved_comment = models.BooleanField(default=False)

	rating = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(5)])

	def approve(self):
		self.approved_comment = True
		self.save

	def __str__(self):
		return self.text

	class Meta:
		verbose_name = 'Review'