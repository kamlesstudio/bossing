import secrets


class AppTokenGenerator():
	def generate_token(self):
		return secrets.token_urlsafe(16)


token_generator = AppTokenGenerator()