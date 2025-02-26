from django.test import TestCase
from django.utils.dateparse import parse_datetime
from .models import Note  

class NoteAPITestCase(TestCase):
    
    def setUp(self):
        """
        สร้าง Note ตัวอย่างสำหรับใช้ในการทดสอบ
        """
        self.note = Note.objects.create(
            name="Introduction to Django",
            file_url="https://example.com/django-intro.pdf",
            thumbnail_url="https://example.com/django-thumbnail.jpg",
            tags="django,python,web",
            created_at=parse_datetime("2025-02-26T12:00:00Z"),
            updated_at=parse_datetime("2025-02-26T12:00:00Z")
        )

    def test_search_by_name(self):
        """
        ทดสอบค้นหา Note โดยค้นหาจาก field name
        URL: /api/notes/?q=Introduction&field=name
        คาดหวังผลลัพธ์เป็นข้อมูลของ note ที่สร้างขึ้น
        """
        response = self.client.get('/api/notes/', {'q': 'Introduction', 'field': 'name'})
        self.assertEqual(response.status_code, 200)
        result = response.json()
        
        # ลบ created_at และ updated_at ออกจากการตรวจสอบ
        for item in result:
            item.pop('created_at', None)
            item.pop('updated_at', None)
        
        expected = [{
            "id": self.note.id,
            "name": "Introduction to Django",
            "file_url": "https://example.com/django-intro.pdf",
            "thumbnail_url": "https://example.com/django-thumbnail.jpg",
            "tags": "django,python,web"
        }]
        self.assertEqual(result, expected)

    def test_search_by_tags(self):
        """
        ทดสอบค้นหา Note โดยค้นหาจาก field tags
        URL: /api/notes/?q=web&field=tags
        คาดหวังผลลัพธ์เป็นข้อมูลของ note ที่สร้างขึ้น
        """
        response = self.client.get('/api/notes/', {'q': 'web', 'field': 'tags'})
        self.assertEqual(response.status_code, 200)
        result = response.json()
        
        # ลบ created_at และ updated_at ออกจากการตรวจสอบ
        for item in result:
            item.pop('created_at', None)
            item.pop('updated_at', None)
        
        expected = [{
            "id": self.note.id,
            "name": "Introduction to Django",
            "file_url": "https://example.com/django-intro.pdf",
            "thumbnail_url": "https://example.com/django-thumbnail.jpg",
            "tags": "django,python,web"
        }]
        self.assertEqual(result, expected)
