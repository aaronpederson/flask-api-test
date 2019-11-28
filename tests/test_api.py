import pytest


@pytest.mark.parametrize('inp, expected', [
    ('contan', 'contain'),
    ('seroius', 'serious'),
    ('pureli', 'purely'),
    ('dose', 'dose')
])
def test_api(client, inp, expected):
    resp = client.get('/correct/%s' % inp)
    assert resp.status_code == 200
    assert resp.data.decode('utf-8') == '{"correction": "%s"}' % expected
