import pytest 
from core.app_auth.models import User
from django.urls import reverse

@pytest.mark.django_db
def test_user_login(client):
    user = User.objects.create_user(username='testuser', email='example.com', password='mypassword')
    login_url = reverse('app_auth:signin')
    response = client.post(login_url, {'username': 'testuser', 'password': 'mypassword'})
    assert response.status_code == 302
    assert response.url == reverse('quotes:root')

    
@pytest.mark.django_db
def test_user_login_fail(client):
    response = client.post(reverse('app_auth:signin'), {'username': 'wrong', 'password': 'wrong'})
    assert response.status_code == 200  # страница логина перезагрузилась
    assert '_auth_user_id' not in client.session