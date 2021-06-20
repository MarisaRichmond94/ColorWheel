"""Fixture for the fct_genres table."""
from utils.alembic.fixtures.users import users_fixture


genres_fixture = [
    {
        'id': 'ac4ed589-aa8e-41d7-b097-1f9604546411',
        'dim_user_id': users_fixture[0].get('id'),
        'name': 'Action',
        'display_name': 'Action',
        'bucket_name': 'colorwheel_action',
        'is_primary': True
    },
    {
        'id': '31c61b28-17ac-4237-bd94-e599be3c636a',
        'dim_user_id': users_fixture[0].get('id'),
        'name': 'Adventure',
        'display_name': 'Adventure',
        'bucket_name': 'colorwheel_adventure',
        'is_primary': True
    },
    {
        'id': '65d384aa-19ab-42e8-9552-c2727bc43a0b',
        'dim_user_id': users_fixture[0].get('id'),
        'name': 'Fantasy',
        'display_name': 'Fantasy',
        'bucket_name': 'colorwheel_fantasy',
        'is_primary': True
    },
    {
        'id': '75a26213-bf2a-4e4c-90ad-4eded6c65caf',
        'dim_user_id': users_fixture[0].get('id'),
        'name': 'Horror',
        'display_name': 'Horror',
        'bucket_name': 'colorwheel_horror',
        'is_primary': True
    },
    {
        'id': 'cd576f7d-49ed-4704-b0df-fbab8a5550f1',
        'dim_user_id': users_fixture[0].get('id'),
        'name': 'Mystery',
        'display_name': 'Mystery',
        'bucket_name': 'colorwheel_mystery',
        'is_primary': True
    },
    {
        'id': 'e72af16e-0fd8-43d5-bd35-e89a367ca716',
        'dim_user_id': users_fixture[0].get('id'),
        'name': 'Romance',
        'display_name': 'Romance',
        'bucket_name': 'colorwheel_romance',
        'is_primary': True
    },
    {
        'id': '41ff7121-fa06-4d90-b2c6-1c9d3529056d',
        'dim_user_id': users_fixture[0].get('id'),
        'name': 'Science Fiction',
        'display_name': 'Science Fiction',
        'bucket_name': 'colorwheel_science_fiction',
        'is_primary': True
    },
    {
        'id': 'b9f70b50-a975-4d0e-934e-cd3b12d612fe',
        'dim_user_id': users_fixture[0].get('id'),
        'name': 'Thriller',
        'display_name': 'Thriller',
        'bucket_name': 'colorwheel_thriller',
        'is_primary': True
    },
    {
        'id': 'e64218aa-65e0-40a4-8b17-edfe523797fa',
        'dim_user_id': users_fixture[0].get('id'),
        'name': 'Western',
        'display_name': 'Western',
        'bucket_name': 'colorwheel_western',
        'is_primary': True
    },
    {
        'id': 'd9b2bd9f-df00-41b4-adc6-44b9b25668a5',
        'dim_user_id': users_fixture[0].get('id'),
        'name': 'Young Adult',
        'display_name': 'Young Adult',
        'bucket_name': None,
        'is_primary': False
    },
    {
        'id': '339b9ee8-ec6d-4214-8d1d-1df609d4c29e',
        'dim_user_id': users_fixture[0].get('id'),
        'name': 'Middle Age',
        'display_name': 'Middle Age',
        'bucket_name': None,
        'is_primary': False
    },
    {
        'id': 'fec630af-ce0b-4b06-b15f-60a3229af55f',
        'dim_user_id': users_fixture[0].get('id'),
        'name': "Children's",
        'display_name': "Children's",
        'bucket_name': None,
        'is_primary': False
    },
    {
        'id': '35eb3485-a121-4e2e-a8b2-2cc0425ee1d4',
        'dim_user_id': users_fixture[0].get('id'),
        'name': 'Contemporary',
        'display_name': 'Contemporary',
        'bucket_name': None,
        'is_primary': False
    },
    {
        'id': '38b9627a-7d99-4df9-bb82-03e99591e2f2',
        'dim_user_id': users_fixture[0].get('id'),
        'name': 'Historical',
        'display_name': 'Historical',
        'bucket_name': None,
        'is_primary': False
    },
    {
        'id': '0050f266-42c9-467e-9ddc-caf3eefc7d56',
        'dim_user_id': users_fixture[0].get('id'),
        'name': 'Humor',
        'display_name': 'Humor',
        'bucket_name': None,
        'is_primary': False
    },
    {
        'id': '9817675d-c4a0-4e0c-aba8-7ec6c80b6f6f',
        'dim_user_id': users_fixture[0].get('id'),
        'name': 'Psychological Thriller',
        'display_name': 'Psychological Thriller',
        'bucket_name': None,
        'is_primary': False
    },
    {
        'id': '9c39fda9-dd15-4f5e-a0e2-2d9890c68200',
        'dim_user_id': users_fixture[0].get('id'),
        'name': 'Paranormal',
        'display_name': 'Paranormal',
        'bucket_name': None,
        'is_primary': False
    },
    {
        'id': '2c5ea03d-91a5-4bd9-bb11-f94aaf66d6c5',
        'dim_user_id': users_fixture[0].get('id'),
        'name': 'Apocolyptic',
        'display_name': 'Apocolyptic',
        'bucket_name': None,
        'is_primary': False
    },
    {
        'id': '3f0b5a59-4cbd-4fa3-b032-9dea274ed43b',
        'dim_user_id': users_fixture[0].get('id'),
        'name': 'Post-Apocolyptic',
        'display_name': 'Post-Apocolyptic',
        'bucket_name': None,
        'is_primary': False
    },
    {
        'id': '23bc3a1d-464d-4be6-9205-8286a05d5093',
        'dim_user_id': users_fixture[0].get('id'),
        'name': 'Dystopian',
        'display_name': 'Dystopian',
        'bucket_name': None,
        'is_primary': False
    }
]
