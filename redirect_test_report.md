# Redirect Test Report
Generated: 2025-08-24

## Summary
- **Total URLs Tested**: 18
- **Successful Redirects**: 13 (72%)
- **Failed/404**: 2 (11%)
- **JavaScript Redirects**: 3 (17%)

## Test Results

### ✅ Successful HTTP 301 Redirects (Working as Expected)
These URLs return HTTP 301 and redirect to the correct destination:

1. **https://targz.fr/color-wheel-chaos**
   - Status: HTTP 301 → HTTP 200
   - Redirects to: /portfolio/2023/11/04/color-wheel-chaos.html

2. **https://targz.fr/monochrome-moire**
   - Status: HTTP 301 → HTTP 200
   - Redirects to: /portfolio/2023/05/13/monochrome-moire-n-1.html

3. **https://targz.fr/chromatic-interplay-n6-half**
   - Status: HTTP 301 → HTTP 200
   - Redirects to: /portfolio/2023/05/01/chromatic-interplay-n-6-half.html

4. **https://targz.fr/strikes**
   - Status: HTTP 301 → HTTP 200
   - Redirects to: /portfolio/2024/06/04/strikes.html

5. **https://targz.fr/grow-2018-interactive-instalation**
   - Status: HTTP 301 → HTTP 200
   - Redirects to: /exhibitions/2018/11/01/fill-the-blank.html

6. **https://targz.fr/amoeba**
   - Status: HTTP 301 → HTTP 200
   - Redirects to: /portfolio/2023/12/17/amoeba.html

7. **https://targz.fr/a-tale-from-the-book-of-christmas-2020**
   - Status: HTTP 301 → HTTP 200
   - Redirects to: /bits/2020/12/01/a-tale-from-the-book-of-christmas-2020.html

### ⚡ JavaScript/Meta Redirects (Working via Client-Side)
These URLs return HTTP 200 with JavaScript/meta refresh redirects:

1. **https://targz.fr/bits/2019/01/01/keep-calm.html**
   - Status: HTTP 200 (with JS redirect)
   - Redirects to: /bits/2012/03/07/keep-calm.html

2. **https://targz.fr/bits/2019/02/01/twittearth.html**
   - Status: HTTP 200 (with JS redirect)
   - Redirects to: /bits/2009/02/01/twittearth.html

3. **https://targz.fr/bits/2021/05/01/stay-yound-and-play-lego.html**
   - Status: HTTP 200 (with JS redirect)
   - Redirects to: /bits/2016/07/05/stay-yound-and-play-lego.html

4. **https://targz.fr/work/**
   - Status: HTTP 200 (with JS redirect)
   - Redirects to: /works/

### ✅ Working Direct URLs (Existing Redirects)
These direct URLs work (they have existing redirect pages):

1. **https://targz.fr/ruinart-anamorphosis/** - HTTP 200
2. **https://targz.fr/wonderbra-decoder/** - HTTP 200
3. **https://targz.fr/la-poste-ces-2017/** - HTTP 200
4. **https://targz.fr/nissan-booster/** - HTTP 200
5. **https://targz.fr/works/** - HTTP 200

### ❌ Still Returning 404
These URLs still need attention:

1. **https://targz.fr/work/ruinart-anamorphosis/** - HTTP 404
   - Note: The direct URL /ruinart-anamorphosis/ works

2. **https://targz.fr/work/wonderbra-decoder/** - HTTP 404
   - Note: The direct URL /wonderbra-decoder/ works

## Recommendations

1. **Work Subdirectory Issue**: URLs with `/work/[project-name]/` pattern are still returning 404. These need special handling since the existing redirect pages are at the root level, not under /work/.

2. **JavaScript Redirects**: The bits/ redirects are using JavaScript/meta refresh redirects (HTTP 200 with client-side redirect) rather than server-side HTTP 301 redirects. This works but is less optimal for SEO.

3. **Consider Server-Side Redirects**: For better SEO and performance, consider implementing server-side redirects (HTTP 301) using:
   - Jekyll redirect plugin
   - Netlify _redirects file (if using Netlify)
   - GitHub Pages redirect configuration

## Conclusion
Most redirects are working successfully. The main issues are:
- `/work/[project-name]/` patterns need additional redirect handling
- Some redirects use JavaScript instead of HTTP 301 (works but less optimal)