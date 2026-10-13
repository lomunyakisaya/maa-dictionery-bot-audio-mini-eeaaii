from django.db import models


class MaaData(models.Model):

    # =========================
    # CHOICES
    # =========================

    PART_OF_SPEECH_CHOICES = [
        ("noun", "Noun"),
        ("verb", "Verb"),
        ("adjective", "Adjective"),
        ("adverb", "Adverb"),
        ("pronoun", "Pronoun"),
        ("preposition", "Preposition"),
        ("conjunction", "Conjunction"),
        ("interjection", "Interjection"),
        ("other", "Other"),
    ]

    DIALECT_CHOICES = [
        ("loitoktok", "Maasai-Loitoktok"),
        ("kaputiei", "Maasai-Kaputiei"),
        ("loodokilani", "Maasai-Loodokilani"),
        ("tanzania", "Maasai-Tz"),
        ("narok", "Maasai-Narok"),
    ]

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("reviewed", "Reviewed"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    ]

    # =========================
    # BASIC LANGUAGE DATA
    # =========================

    word = models.CharField(
        max_length=255
    )

    meaning = models.TextField()

    context = models.TextField(
        blank=True,
        help_text="Example sentence or situation where the word is used."
    )

    part_of_speech = models.CharField(
        max_length=30,
        choices=PART_OF_SPEECH_CHOICES,
        blank=True
    )

    # =========================
    # TRANSLATION
    # =========================

    english_translation = models.TextField(
        blank=True
    )

    swahili_translation = models.TextField(
        blank=True
    )

    # =========================
    # DIALECT / REGION
    # =========================

    dialect = models.CharField(
        max_length=30,
        choices=DIALECT_CHOICES,
        blank=True
    )

    region = models.CharField(
        max_length=100,
        blank=True
    )

    # =========================
    # AUDIO
    # =========================

    audio = models.FileField(
        upload_to="maa/audio/",
        blank=True,
        null=True
    )

    # =========================
    # DATA SOURCE
    # =========================

    contributor_name = models.CharField(
        max_length=255,
        blank=True
    )

    source = models.CharField(
        max_length=255,
        blank=True,
        help_text="Where this data came from."
    )

    # =========================
    # VALIDATION
    # =========================

    is_verified = models.BooleanField(
        default=False
    )

    verification_notes = models.TextField(
        blank=True
    )

    # =========================
    # DATA STATUS
    # =========================

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    # =========================
    # TIMESTAMPS
    # =========================

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    # =========================
    # REPRESENTATION
    # =========================

    def __str__(self):
        return self.word