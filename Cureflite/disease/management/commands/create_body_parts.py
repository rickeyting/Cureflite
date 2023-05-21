from django.core.management.base import BaseCommand
from disease.models import BodyParts


class Command(BaseCommand):
    help = 'Create BodyParts instances'

    def handle(self, *args, **options):
        body_parts = [
            {'chinese_name': '頭部', 'english_name': 'head'},
            {'chinese_name': '眼睛', 'english_name': 'eyes'},
            {'chinese_name': '鼻子', 'english_name': 'nose'},
            {'chinese_name': '嘴巴', 'english_name': 'mouth'},
            {'chinese_name': '肩膀', 'english_name': 'shoulder'},
            {'chinese_name': '胸部', 'english_name': 'chest'},
            {'chinese_name': '腹部', 'english_name': 'abdomen'},
            {'chinese_name': '骨盆', 'english_name': 'pelvis'},
            {'chinese_name': '手臂', 'english_name': 'arms'},
            {'chinese_name': '手', 'english_name': 'hands'},
            {'chinese_name': '腿', 'english_name': 'legs'},
            {'chinese_name': '腳', 'english_name': 'feet'},
            {'chinese_name': '皮膚', 'english_name': 'skin'},
        ]

        for part in body_parts:
            body_part = BodyParts.objects.create(
                chinese_name=part['chinese_name'],
                english_name=part['english_name'],
            )
            body_part.save()

            self.stdout.write(self.style.SUCCESS(f"Created BodyPart: {body_part}"))


