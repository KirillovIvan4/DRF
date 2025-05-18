from rest_framework.serializers import ValidationError
from urllib.parse import urlparse


allowed_video_link = [
    'www.youtube.com',
]


def validate_youtube_link(value):
    if not value:
        return

    parsed = urlparse(value)

    # Проверяем домен
    if parsed.netloc not in ['youtube.com', 'www.youtube.com', 'youtu.be']:
        raise ValidationError("Допустимы только ссылки на YouTube")

    # Проверяем схему (http/https)
    if parsed.scheme not in ['http', 'https']:
        raise ValidationError(
            "Ссылка должна начинаться с http:// или https://")
