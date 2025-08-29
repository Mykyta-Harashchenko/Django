import pytest 
from core.app_auth.models import User
from django.urls import reverse
from django.core import mail



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
    
@pytest.mark.django_db
def test_forgot_password_feature(client):
    user = User.objects.create_user(username='testuser1', email='example1@example.com', password='mypassword')
    url = reverse('app_auth:reset_password')
    response = client.post(url, {'email': user.email})
    assert response.status_code == 302
    assert response.url == reverse('app_auth:password_reset_done')
    assert len(mail.outbox) == 1
    email = mail.outbox[0]
    body = email.body
    
    assert user.email in email.to
    assert 'reset your password' in email.subject.lower() or 'password' in email.subject.lower()
    assert user.username in body