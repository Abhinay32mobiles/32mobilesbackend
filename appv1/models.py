import uuid
from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
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
        ("Vivo", 'Vivo'),
        ("Realme", 'Realme'),
        ("Oppo", 'Oppo'),
        ("Xiaomi", 'Xiaomi'),
        ("OnePlus", 'OnePlus'),
        ('Motorola', 'Motorola'),
        ('Other', 'Other')
        # Add other brands here
    ]
    
    brand_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=50,
        unique=True,
        choices=BRAND_CHOICES
    )
    brand_cdn_link = models.URLField(max_length=500, blank=True, null=True)
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
    

    def __str__(self):
        return self.get_tag_display()

class ModelDetails(models.Model):
    model_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    model_name = models.CharField(max_length=50)
    
    # Define a one-to-many relationship from ModelDetails to Brand
    meta_desc = models.CharField(max_length=500,blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, default=uuid.uuid4())
    price = models.DecimalField(max_digits=10, decimal_places=2, default=10000.00)
    currency = models.CharField(max_length=30,blank=True)
    # Define a one-to-many relationship from ModelDetails to Category
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=uuid.uuid4())
    screen_size = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    resolution = models.CharField(max_length=50, null=True, blank=True)
    processor = models.CharField(max_length=50, null=True, blank=True)
    ram = models.PositiveSmallIntegerField(null=True, blank=True)
    storage_capacity = models.PositiveIntegerField(null=True, blank=True)
    camera_resolution = models.CharField(max_length=200, null=True, blank=True)
    front_camera_resolution = models.CharField(max_length=100, null=True, blank=True)
    back_camera_resolution = models.CharField(max_length=100, null=True, blank=True)
    battery_capacity = models.PositiveSmallIntegerField(null=True, blank=True)
    operating_system = models.CharField(max_length=200, null=True, blank=True)
    weight = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    dimensions = models.CharField(max_length=100, null=True, blank=True)
    color = models.CharField(max_length=100, null=True, blank=True)
    connectivity = models.TextField(null=True, blank=True)
    expandable_storage = models.BooleanField(default=False)
    sim_card_slots = models.CharField(max_length=100, null=True, blank=True)
    network_connectivity = models.CharField(max_length=100, null=True, blank=True)
    bluetooth_version = models.CharField(max_length=100, null=True, blank=True)
    wi_fi = models.CharField(max_length=100, null=True, blank=True)
    nfc = models.BooleanField(default=False)
    biometric_security = models.CharField(max_length=100, null=True, blank=True)
    water_resistance = models.CharField(max_length=100, null=True, blank=True)
    dust_resistance = models.CharField(max_length=100, null=True, blank=True)
    audio_jack = models.CharField(max_length=100, null=True, blank=True)
    speaker_quality = models.CharField(max_length=100, null=True, blank=True)
    gps = models.BooleanField(default=False)
    sensors = models.CharField(max_length=100, null=True, blank=True)
    wireless_charging = models.BooleanField(default=False)
    os_updates = models.BooleanField(default=False)
    battery_life = models.CharField(max_length=50, null=True, blank=True)
    color_options = ArrayField(
        models.CharField(max_length=7),  #strings like "#RRGGBB"
        blank=True,
        default=list
    )
    buylink1 = models.URLField(max_length=500, blank=True, null=True)
    buylink2 = models.URLField(max_length=500, blank=True, null=True)
    buylink3 = models.URLField(max_length=500, blank=True, null=True)
    buylink4 = models.URLField(max_length=500, blank=True, null=True)
    img1 = models.URLField(max_length=500, blank=False, null=False)
    img2 = models.URLField(max_length=500, blank=True, null=True)
    img3 = models.URLField(max_length=500, blank=True, null=True)
    img4 = models.URLField(max_length=500, blank=True, null=True)
    price_range = models.CharField(max_length=50, null=True, blank=True)
    warranty = models.TextField(null=True, blank=True)
    special_features = models.TextField(null=True, blank=True)
    gaming_performance = models.CharField(max_length=500, null=True, blank=True)
    brandname = models.CharField(max_length=50, blank=True, null=True, default="just a brand")
    antudesc= models.TextField(blank=True, null=True),
    antuscore =models.PositiveIntegerField(blank=True, null=True),
    # ... other fields ...
    categoryname = models.CharField(max_length=50, blank=True, null=True)
    # ... other fields ...
    tags = models.ManyToManyField(TagsModel, related_name='modeldetails')
    def save(self, *args, **kwargs):
        self.categoryname = self.categoryname.lower() if self.categoryname else self.categoryname
        self.brandname = self.brandname.lower() if self.brandname else self.brandname
        super(ModelDetails, self).save(*args, **kwargs)

    
    def __str__(self):
        return self.model_name



class CategoryBrandRelation(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
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
    

    def __str__(self):
        return self.tag

class Article(models.Model):
    article_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=500)
    sub_title1 = models.CharField(max_length=500,blank=True)
    sub_title2 = models.CharField(max_length=500,blank=True)
    sub_title3 = models.CharField(max_length=500,blank=True)
    sub_title4 = models.CharField(max_length=500,blank=True)
    meta_desc = models.CharField(max_length=500,blank=True)
    author_name = models.CharField(max_length=500,blank=True)
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
    image_url = models.URLField(max_length=500, blank=False)
    image_url1 = models.URLField(max_length=500, blank=True)
    image_url2 = models.URLField(max_length=500, blank=True)
    image_url3 = models.URLField(max_length=500, blank=True)
    tags = models.ManyToManyField(TagsArticle, related_name='articles')
    def __str__(self):
        return self.title
    # tags = models.ManyToManyField(Tag, blank=True)
class YouTubeVideoDetails(models.Model):
    video_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    meta_desc = models.CharField(max_length=500,blank=True)
    SHORT = 'short'
    LONG = 'long'
    YES = 'Yes'
    NO = 'No'
    VIDEO_TYPE_CHOICES = [
        (SHORT, 'Short'),
        (LONG, 'Long'),
    ]

    # Type field with choices
    type = models.CharField(max_length=10, choices=VIDEO_TYPE_CHOICES, default=SHORT)
    video_url = models.URLField(blank=True, null=True)
    thumbnail_url = models.URLField(blank=True, null=True)
    # Define a one-to-one relationship from YouTubeVideo to ModelDetails
    model_details = models.ForeignKey(ModelDetails, on_delete=models.CASCADE,default = uuid.uuid4(),related_name='ytvideos')
    
    # Define a many-to-one relationship from YouTubeVideo to Category
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True,related_name="ytvideo")
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True, blank=True,related_name="ytvideo")
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True,related_name="ytvideo")
    recom = models.CharField(max_length=3, choices=[(YES, 'Yes'), (NO, 'No')], default=NO)
    duration = models.CharField(max_length=10,default="10min")
    upload_datetime = models.DateTimeField(null=True, blank=True,default=timezone.now)


class Statics(models.Model):
    homepage_cdn_links = ArrayField(models.URLField(max_length=400), blank=True, null=True, size=15)
    homepage_redirect_links = ArrayField(models.URLField(max_length=400), blank=True, null=True, size=15)
    homepage_banner_text = ArrayField(models.CharField(max_length=400), blank=True, null=True, size=15)
    homepage_button_text = ArrayField(models.CharField(max_length=400), blank=True, null=True, size=15)
    homepagevert_cdn_links = ArrayField(models.URLField(max_length=400), blank=True, null=True, size=5)
    homepagevert_redirect_links = ArrayField(models.URLField(max_length=400), blank=True, null=True, size=5)
    homepagevert_banner_text = ArrayField(models.CharField(max_length=400), blank=True, null=True, size=5)
    homepagevert_button_text = ArrayField(models.CharField(max_length=400), blank=True, null=True, size=5)
    homepagehori_cdn_links = ArrayField(models.URLField(max_length=400), blank=True, null=True, size=5)
    homepagehori_redirect_links = ArrayField(models.URLField(max_length=400), blank=True, null=True, size=5)
    homepagehori_banner_text = ArrayField(models.CharField(max_length=400), blank=True, null=True, size=5)
    homepagehori_button_text = ArrayField(models.CharField(max_length=400), blank=True, null=True, size=5)
    homepage_brand_banner_cdn = ArrayField(models.URLField(max_length=400), blank=True, null=True, size=15)
    #articles
    articles_cdn_links = ArrayField(models.URLField(max_length=400), blank=True, null=True, size=15)
    articles_redirect_links = ArrayField(models.URLField(max_length=400), blank=True, null=True, size=15)
    articles_banner_text = ArrayField(models.CharField(max_length=400), blank=True, null=True, size=15)
    articles_button_text = ArrayField(models.CharField(max_length=400), blank=True, null=True, size=15)
    artilcevert_cdn_links = ArrayField(models.URLField(max_length=400), blank=True, null=True, size=5)
    artilcevert_redirect_links = ArrayField(models.URLField(max_length=400), blank=True, null=True, size=5)
    artilcevert_banner_text = ArrayField(models.CharField(max_length=400), blank=True, null=True, size=5)
    artilcevert_button_text = ArrayField(models.CharField(max_length=400), blank=True, null=True, size=5)
    artilcehori_cdn_links = ArrayField(models.URLField(max_length=400), blank=True, null=True, size=5)
    artilcehori_redirect_links = ArrayField(models.URLField(max_length=400), blank=True, null=True, size=5)
    artilcehori_banner_text = ArrayField(models.CharField(max_length=400), blank=True, null=True, size=5)
    artilcehori_button_text = ArrayField(models.CharField(max_length=400), blank=True, null=True, size=5)
    # artilce_brand_banner_cdn = ArrayField(models.CharField(max_length=200), blank=True, null=True, size=15)
    #products
    products_cdn_links = ArrayField(models.URLField(max_length=400), blank=True, null=True, size=15)
    products_redirect_links = ArrayField(models.URLField(max_length=400), blank=True, null=True, size=15)
    products_banner_text = ArrayField(models.CharField(max_length=400), blank=True, null=True, size=15)
    products_button_text = ArrayField(models.CharField(max_length=400), blank=True, null=True, size=15)
    productvert_cdn_links = ArrayField(models.URLField(max_length=400), blank=True, null=True, size=5)
    productvert_redirect_links = ArrayField(models.URLField(max_length=400), blank=True, null=True, size=5)
    productvert_banner_text = ArrayField(models.CharField(max_length=400), blank=True, null=True, size=5)
    productvert_button_text = ArrayField(models.CharField(max_length=400), blank=True, null=True, size=5)
    producthori_cdn_links = ArrayField(models.URLField(max_length=400), blank=True, null=True, size=5)
    producthori_redirect_links = ArrayField(models.URLField(max_length=400), blank=True, null=True, size=5)
    producthori_banner_text = ArrayField(models.CharField(max_length=400), blank=True, null=True, size=5)
    producthori_button_text = ArrayField(models.CharField(max_length=400), blank=True, null=True, size=5)
    # product_brand_banner_cdn = ArrayField(models.CharField(max_length=200), blank=True, null=True, size=15)
    #price bands array
    product_priceband_array = ArrayField(models.PositiveIntegerField(), blank=True, null=True, size=15)

class Contactdetails(models.Model):
    person_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField()

    def __str__(self):
        return self.name


