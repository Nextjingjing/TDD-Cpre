from django.db import models

class Note(models.Model):  
    name = models.CharField(max_length=255)  # Note title
    file_url = models.URLField()  # URL where the file is stored (Google Drive, S3, etc.)
    thumbnail_url = models.URLField(blank=True, null=True)  # Thumbnail for preview
    tags = models.CharField(max_length=255, blank=True, null=True)  # Searchable tags (comma-separated)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"

    def __str__(self):
        return self.name
