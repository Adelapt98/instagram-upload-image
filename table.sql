create database instabot;

-----------

create table page
(
    id           serial not null,
    username     text,
    last_post_id text,
    is_deleted   boolean
);

----------

create table post
(
    id               serial not null,
    short_code       text,
    username         text,
    inserted_date    integer,
    file_address     text,
    caption          text,
    is_video         boolean,
    is_deleted       boolean,
    is_posted        boolean,
    caption_hashtags text[]
);

