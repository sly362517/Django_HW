import logging

from django.http import HttpResponse

# Create your views here.

logger = logging.getLogger(__name__)

headers = {'Cache-Control': 'no-cache, must-revalidate',
           'Pragma': 'no-cache'}


def main(request):
    body = """
    <title>Главная страница</title>
    <body>
        <div>
            <h1>Главная страница</h1>
            <p>Содержимое главной страницы</p>
            <p>Перейдите на страницу: /about_me</p>
        </div>
        <footer>
            <div>
                <p>Copyright &copy;
                    <script type="text/javascript"> document.write(new Date().getFullYear());</script>
                    Communications Inc. Все права защищены.
                </p>
            </div>
        </footer>
    </body>
    """
    logger.info(f'Страница открыта: {body}')
    return HttpResponse(body, charset="utf-8", headers=headers)


def aboutme(request):
    body = """
        <title>О себе</title>  
        <body>     
            <div>
                <h1>Махортов Дмитрий Николаевич</h1>
                <p>Мужчина, 25 лет, родился 4 апреля 1998</p>
                <p>Перейдите на страницу: /main</p>
            </div>
            <footer>
                <div>
                    <p>Copyright &copy;
                        <script type="text/javascript"> document.write(new Date().getFullYear());</script>
                        Communications Inc. Все права защищены.
                    </p>
                </div>
            </footer>
        </body>
        """
    logger.info(f'Страница открыта: {body}')
    return HttpResponse(body, charset="utf-8", headers=headers)

