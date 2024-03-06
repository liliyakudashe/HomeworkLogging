import requests as rq
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger('RequestsLogger')



sites = [
         'https://www.youtube.com/',
         'https://instagram.com',
         'https://wikipedia.org',
         'https://yahoo.com',
         'https://yandex.ru',
         'https://whatsapp.com',
         'https://twitter.com',
         'https://amazon.com',
         'https://tiktok.com',
         'https://www.ozon.ru']


# def make_request(url):
#     try:
#         response = rq.get(url, timeout=3)
#         if response.status_code == 200:
#             logger.info(f"{url}, response - {response.status_code}")
#             with open('success_responses.log', 'a') as f:
#                 f.write(f"INFO: '{url}', response - {response.status_code}\n")
#         else:
#             logger.warning(f"{url}, response - {response.status_code}")
#             with open('bad_responses.log', 'a') as f:
#                 f.write(f"WARNING: '{url}', response - {response.status_code}\n")
#     except rq.exceptions.RequestException:
#         logger.error(f"{url}, NO CONNECTION")
#         with open('blocked_responses.log', 'a') as f:
#             f.write(f"ERROR: {url}, NO CONNECTION\n")


for site in sites:
    try:
        response = rq.get(site, timeout=3)
        if response.status_code == 200:
            logger.info(f' {site}, response - {response.status_code}')
        else:
            logger.warning(f'{site}, response - {response.status_code}')
    except rq.exceptions.RequestException:
        logger.error(f' {site}, NO CONNECTION')
