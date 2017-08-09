from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin

import symposion.views


urlpatterns = [
    url(r"^$", TemplateView.as_view(template_name="static_pages/homepage.html"), name="home"),
    url(r"^code-of-conduct$", TemplateView.as_view(template_name="static_pages/code-of-conduct.html"), name="code-of-conduct"),
    url(r"^about$", TemplateView.as_view(template_name="static_pages/about.html"), name="about"),
    url(r"^news$", TemplateView.as_view(template_name="static_pages/news.html"), name="news"),
    url(r"^admin/", include(admin.site.urls)),

    url(r"^account/", include("account.urls")),

    url(r"^dashboard/", symposion.views.dashboard, name="dashboard"),

    url(r"^speaker/", include("symposion.speakers.urls")),
    url(r"^proposals/", include("symposion.proposals.urls")),
    url(r"^proposals$", TemplateView.as_view(template_name="static_pages/proposals.html"), name="proposals"),
    url(r"^selection-process$", TemplateView.as_view(template_name="static_pages/selection-process.html"), name="selection-process"),
    url(r"^sponsors/", include("symposion.sponsorship.urls")),
    url(r"^sponsors$", TemplateView.as_view(template_name="static_pages/sponsors.html"), name="sponsors"),
    url(r"^reviews/", include("symposion.reviews.urls")),
    url(r"^schedule/", include("symposion.schedule.urls")),

    url(r"^teams/", include("symposion.teams.urls")),

    # Demo payment gateway and related features
    url(r"^register/pinaxcon/", include("pinaxcon.registrasion.urls")),

    # Demo payment gateway and related features
    url(r"^register/payments/", include("registripe.urls")),

    # Required by registrasion
    url(r'^register/', include('registrasion.urls')),
    url(r'^nested_admin/', include('nested_admin.urls')),

    # Catch-all MUST go last.
    #url(r"^", include("pinax.pages.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
