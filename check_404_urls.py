#!/usr/bin/env python3

import csv
import requests
import time
from datetime import datetime
from urllib.parse import urlparse

def check_url(url, timeout=10):
    """Check if a URL returns a valid response."""
    try:
        response = requests.get(url, timeout=timeout, allow_redirects=True)
        return {
            'url': url,
            'status_code': response.status_code,
            'final_url': response.url,
            'redirected': url != response.url,
            'error': None
        }
    except requests.exceptions.RequestException as e:
        return {
            'url': url,
            'status_code': None,
            'final_url': None,
            'redirected': False,
            'error': str(e)
        }

def main():
    # Read the CSV file
    with open('404V2.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        urls = list(csv_reader)
    
    # Separate URLs by domain
    targz_urls = []
    shop_urls = []
    
    for row in urls:
        url = row['URL']
        if 'shop.targz.fr' in url:
            shop_urls.append(row)
        else:
            targz_urls.append(row)
    
    # Check targz.fr URLs
    print("=" * 80)
    print("CHECKING TARGZ.FR URLS")
    print("=" * 80)
    print(f"Total URLs to check: {len(targz_urls)}\n")
    
    targz_results = []
    for i, row in enumerate(targz_urls, 1):
        url = row['URL']
        print(f"[{i}/{len(targz_urls)}] Checking: {url}")
        result = check_url(url)
        result['last_crawled'] = row['Last crawled']
        result['csv_status'] = row['Status']
        targz_results.append(result)
        time.sleep(0.5)  # Be polite to the server
    
    # Generate targz.fr report
    with open('targz_fr_report.txt', 'w') as report:
        report.write(f"TARGZ.FR 404 CHECK REPORT\n")
        report.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        report.write("=" * 80 + "\n\n")
        
        # Summary
        working = [r for r in targz_results if r['status_code'] and r['status_code'] < 400]
        redirects = [r for r in targz_results if r['redirected']]
        errors_404 = [r for r in targz_results if r['status_code'] == 404]
        other_errors = [r for r in targz_results if r['error'] or (r['status_code'] and r['status_code'] >= 400 and r['status_code'] != 404)]
        
        report.write(f"SUMMARY:\n")
        report.write(f"  Total URLs checked: {len(targz_results)}\n")
        report.write(f"  Working (2xx/3xx): {len(working)}\n")
        report.write(f"  Redirected: {len(redirects)}\n")
        report.write(f"  404 Errors: {len(errors_404)}\n")
        report.write(f"  Other Errors: {len(other_errors)}\n\n")
        
        # Detailed results
        report.write("URLS NEEDING FIXES (404s):\n")
        report.write("-" * 40 + "\n")
        for result in errors_404:
            report.write(f"❌ {result['url']}\n")
            report.write(f"   Status: 404 Not Found\n")
            report.write(f"   Last crawled: {result['last_crawled']}\n\n")
        
        if not errors_404:
            report.write("No 404 errors found!\n\n")
        
        report.write("\nWORKING URLS:\n")
        report.write("-" * 40 + "\n")
        for result in working:
            status = "✅" if result['status_code'] == 200 else "↪️"
            report.write(f"{status} {result['url']}\n")
            report.write(f"   Status: {result['status_code']}\n")
            if result['redirected']:
                report.write(f"   Redirected to: {result['final_url']}\n")
            report.write("\n")
        
        if other_errors:
            report.write("\nOTHER ERRORS:\n")
            report.write("-" * 40 + "\n")
            for result in other_errors:
                report.write(f"⚠️  {result['url']}\n")
                if result['status_code']:
                    report.write(f"   Status: {result['status_code']}\n")
                if result['error']:
                    report.write(f"   Error: {result['error']}\n")
                report.write("\n")
    
    print(f"\n✅ Targz.fr report saved to: targz_fr_report.txt")
    
    # Check shop.targz.fr URLs
    print("\n" + "=" * 80)
    print("CHECKING SHOP.TARGZ.FR URLS")
    print("=" * 80)
    print(f"Total URLs to check: {len(shop_urls)}\n")
    
    shop_results = []
    for i, row in enumerate(shop_urls, 1):
        url = row['URL']
        print(f"[{i}/{len(shop_urls)}] Checking: {url}")
        result = check_url(url)
        result['last_crawled'] = row['Last crawled']
        result['csv_status'] = row['Status']
        shop_results.append(result)
        time.sleep(0.5)
    
    # Generate shop.targz.fr report
    with open('shop_targz_fr_report.txt', 'w') as report:
        report.write(f"SHOP.TARGZ.FR 404 CHECK REPORT\n")
        report.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        report.write("=" * 80 + "\n\n")
        
        # Summary
        working = [r for r in shop_results if r['status_code'] and r['status_code'] < 400]
        redirects = [r for r in shop_results if r['redirected']]
        errors_404 = [r for r in shop_results if r['status_code'] == 404]
        other_errors = [r for r in shop_results if r['error'] or (r['status_code'] and r['status_code'] >= 400 and r['status_code'] != 404)]
        
        report.write(f"SUMMARY:\n")
        report.write(f"  Total URLs checked: {len(shop_results)}\n")
        report.write(f"  Working (2xx/3xx): {len(working)}\n")
        report.write(f"  Redirected: {len(redirects)}\n")
        report.write(f"  404 Errors: {len(errors_404)}\n")
        report.write(f"  Other Errors: {len(other_errors)}\n\n")
        
        report.write("NOTE: Some shop.targz.fr URLs contain patterns/wildcards that may not be\n")
        report.write("      actual URLs but rather patterns for blocking/routing.\n\n")
        
        # Detailed results
        report.write("URLS NEEDING FIXES (404s):\n")
        report.write("-" * 40 + "\n")
        for result in errors_404:
            report.write(f"❌ {result['url']}\n")
            report.write(f"   Status: 404 Not Found\n")
            report.write(f"   Last crawled: {result['last_crawled']}\n\n")
        
        if not errors_404:
            report.write("No 404 errors found!\n\n")
        
        report.write("\nWORKING URLS:\n")
        report.write("-" * 40 + "\n")
        for result in working:
            status = "✅" if result['status_code'] == 200 else "↪️"
            report.write(f"{status} {result['url']}\n")
            report.write(f"   Status: {result['status_code']}\n")
            if result['redirected']:
                report.write(f"   Redirected to: {result['final_url']}\n")
            report.write("\n")
        
        if other_errors:
            report.write("\nOTHER ERRORS:\n")
            report.write("-" * 40 + "\n")
            for result in other_errors:
                report.write(f"⚠️  {result['url']}\n")
                if result['status_code']:
                    report.write(f"   Status: {result['status_code']}\n")
                if result['error']:
                    report.write(f"   Error: {result['error']}\n")
                report.write("\n")
    
    print(f"✅ Shop.targz.fr report saved to: shop_targz_fr_report.txt")
    print("\n✅ All checks completed!")

if __name__ == "__main__":
    main()