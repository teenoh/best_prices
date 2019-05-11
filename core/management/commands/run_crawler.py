import os
from django.core.management.base import BaseCommand
from core.models import JumiaItem


def run_crawler():
    os.system('cd best_prices_spider && scrapy crawl jumia')
    return


class Command(BaseCommand):
    def handle(self, **options):
        run_crawler()
