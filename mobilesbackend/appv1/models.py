import uuid
from django.db import models
from django.utils import timezone
default_brand_uuid = uuid.uuid4()
class Brand(models.Model):
    SAMSUNG = 'Samsung'
    APPLE = 'Apple'
    GOOGLE = 'Google'
    # Add other brands as needed
    
    BRAND_CHOICES = [
        (SAMSUNG, 'Samsung'),
        (APPLE, 'Apple'),
        (GOOGLE, 'Google'),
        # Add other brands here
    ]
    
    brand_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=50,
        unique=True,
        choices=BRAND_CHOICES
    )
    def __str__(self):
        return self.name
class Mobile(models.Model):
    mobile_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    model_name = models.CharField(max_length=50)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)

class TV(models.Model):
    tv_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    model_name = models.CharField(max_length=50)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)

class Category(models.Model):
    MOBILE = 'Mobile'
    TV1 = 'TV'
    
    CATEGORY_CHOICES = [
        (MOBILE, 'Mobile'),
        (TV1, 'TV'),
    ]
    
    category_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=50,
        unique=True,
        choices=CATEGORY_CHOICES
    )
    def __str__(self):
        return self.name
    
    # Conditional ForeignKeys
    
    # modeldetails = models.ForeignKey(ModelDetails, on_delete=models.SET_NULL, null=True, blank=True)


class ModelDetails(models.Model):
    model_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    model_name = models.CharField(max_length=50)
    
    # Define a one-to-many relationship from ModelDetails to Brand
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, default=uuid.uuid4())
    price = models.DecimalField(max_digits=10, decimal_places=2, default=10000.00)
    # Define a one-to-many relationship from ModelDetails to Category
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=uuid.uuid4())
    screen_size = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    resolution = models.CharField(max_length=50, null=True, blank=True)
    processor = models.CharField(max_length=50, null=True, blank=True)
    RAM = models.PositiveSmallIntegerField(null=True, blank=True)
    storage_capacity = models.PositiveIntegerField(null=True, blank=True)
    camera_resolution = models.CharField(max_length=50, null=True, blank=True)
    battery_capacity = models.PositiveSmallIntegerField(null=True, blank=True)
    operating_system = models.CharField(max_length=50, null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    dimensions = models.CharField(max_length=100, null=True, blank=True)
    color = models.CharField(max_length=20, null=True, blank=True)
    connectivity = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.model_name



class CategoryBrandRelation(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Article(models.Model):
    article_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    content = models.TextField(null=False, blank = False)
    content2 = models.TextField(default="")
    content3 = models.TextField(default="")
    content4 = models.TextField(default="")
    publication_date = models.DateField(default = timezone.now)
    products = models.ManyToManyField(ModelDetails, blank=True)
    brands = models.ManyToManyField(Brand, blank=True)  # Changed to ManyToManyField
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    image_url = models.URLField(max_length=200, blank=False)
    image_url1 = models.URLField(max_length=200, blank=True)
    image_url2 = models.URLField(max_length=200, blank=True)
    image_url3 = models.URLField(max_length=200, blank=True)
    def __str__(self):
        return self.title
    # tags = models.ManyToManyField(Tag, blank=True)
class YouTubeVideo(models.Model):
    video_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    SHORT = 'short'
    LONG = 'long'
    VIDEO_TYPE_CHOICES = [
        (SHORT, 'Short'),
        (LONG, 'Long'),
    ]

    # Type field with choices
    type = models.CharField(max_length=10, choices=VIDEO_TYPE_CHOICES, default=SHORT)
    video_url = models.URLField(blank=True, null=True)
    # Define a one-to-one relationship from YouTubeVideo to ModelDetails
    model_details = models.ForeignKey(ModelDetails, on_delete=models.CASCADE,default = uuid.uuid4(),related_name='ytvideos')
    
    # Define a many-to-one relationship from YouTubeVideo to Category
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True,related_name="ytvideo")
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True, blank=True,related_name="ytvideo")
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True,related_name="ytvideo")
class TagsModel(models.Model):
    # Predefined tag choices
    TAG_CHOICES = [
        ('Latest', 'Latest'),
        ('BestCamera', 'BestCamera'),
        ('Performance', 'Performance'),
        ('Gaming', 'Gaming'),
        ('Battery', 'Battery'),
        ('Iphone', 'Iphone'),
        ('Samsung', 'Samsung'),
        ('120hz', '120hz'),
        ('90hz', '90hz'),
        ('Nothing', 'Nothing'),
        ('Low-price', 'Low-Price'),
        # Add more tag choices as needed
    ]

    # Fields
    tag = models.CharField(
        max_length=30,
        choices=TAG_CHOICES,
        unique=True,
    )

    # Many-to-many relationship with ModelDetails
    model_details = models.ManyToManyField(ModelDetails, related_name='tags')

    def __str__(self):
        return self.get_tag_display()

class TagsArticle(models.Model):
    # Predefined tag choices
    # articletag_id= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    TAG_CHOICES = [
        ('Latest', 'Latest'),
        ('BestDeals', 'BestDeals'),
        ('Comparison', 'Comparison'),
        ('Upcoming', 'Upcoming'),
        ('HotDeals', 'HotDeals'),
        ('News', 'News'),
        ('Mobiles', 'Mobiles'),
        ('Laptops', 'Laptops'),
        ('Smartwatch', 'Smartwatch'),
        ('Earphones', 'Earphones'),
        ('Gadget', 'Gadget'),
        # Add more tag choices as needed
    ]

    # Fields
    tag = models.CharField(
        max_length=30,
        choices=TAG_CHOICES,
        unique=True,
    )
      # make changes in this model so  that it give the  names  of the   keys when getting mapped to the articles  keys

    # Many-to-many relationship with Article
    articles = models.ManyToManyField(Article, related_name='tags')

    def __str__(self):
        return self.tag
