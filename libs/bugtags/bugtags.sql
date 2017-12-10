DROP TABLE if exists bugtags_main ;
DROP TABLE if exists bugtags_main_tags ;
DROP TABLE if exists bugtags_main_snapshots ;
DROP TABLE if exists bugtags_main_tags_occurrence_info ;
DROP TABLE IF EXISTS bugtags_main_user_data;


CREATE TABLE if not exists bugtags_main
(
hw_id integer PRIMARY KEY autoincrement,
id integer,
app_id integer,
code integer,
description	text,
--uid	integer,
--receiver_uid	integer,
--type	integer,
--status	integer,
updated_at text,
created_at	text --,
--tag_num	integer,
--succ_num	integer,
--user	text,
--crash_num	integer,
--device_num	integer,
--model_num	integer

--tags	[]存入 bugtags_main_tags
--snapshots []存入 bugtags_main_snapshots
);

CREATE TABLE if not exists bugtags_main_tags
(
id integer PRIMARY KEY,
app_id	integer,
issue_id	integer,
code	integer,
snapshot_id	integer, --截图的id?
description	text,
--flag	integer,
--type	integer,
--priority	integer,
--pos	text,
updated_at	text,
created_at	text,
version_name	text,
version_code	text,
issue_code	integer
--dev_user	text, --异常分配的人
--keywords	text,
--duplicate	text,

--occurrence_info	text,--{}用户信息
--snapshot	text, --{}截图信息  存入bugtags_main_snapshots
--crash_extra	text
);

CREATE TABLE if not exists bugtags_main_snapshots
(
id integer PRIMARY KEY,
app_id	integer,
issue_id	integer,
--uid	integer,
url	text,
--meta	text,
created_at	text,
--w	integer,
--h	integer,
has_snapshot	text
);

CREATE TABLE if not exists bugtags_main_tags_occurrence_info
(
hw_id integer PRIMARY KEY autoincrement,

tagid integer, --外面传入

version_name	text,
version_code	text,
release_state	text,
model	text,
time	text,
time_fmt	text,
user_steps	text,--操作步骤
user_data	text,--用户信息
console_log	text,--啥log
crash_log	text
);

CREATE TABLE if not exists bugtags_main_user_data
(
id integer PRIMARY KEY autoincrement,
tagid integer, --外面传入

app_code integer, --当前版本号
name	text,
s_uid	integer,
uid	integer,
s_sid	integer,
appname	text
);


-- DELETE FROM bugtags_main WHERE 1=1;
-- DELETE FROM bugtags_main_tags WHERE 1=1;
-- DELETE FROM bugtags_main_snapshots WHERE 1=1;
-- DELETE FROM bugtags_main_tags_occurrence_info WHERE 1=1;