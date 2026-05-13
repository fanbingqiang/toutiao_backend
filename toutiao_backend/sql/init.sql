-- 新闻分类表
CREATE TABLE IF NOT EXISTS news_categories (
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT '分类ID',
    name VARCHAR(50) NOT NULL UNIQUE COMMENT '分类名称',
    sort_order INT DEFAULT 0 COMMENT '排序',
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间'
) COMMENT '新闻分类表';

-- 新闻表
CREATE TABLE IF NOT EXISTS news (
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT '新闻ID',
    category_id INT NOT NULL COMMENT '分类ID',
    title VARCHAR(200) NOT NULL COMMENT '新闻标题',
    summary VARCHAR(500) DEFAULT '' COMMENT '新闻摘要',
    cover_url VARCHAR(500) DEFAULT '' COMMENT '封面图地址',
    content TEXT COMMENT '新闻内容',
    source VARCHAR(100) DEFAULT '' COMMENT '来源',
    author VARCHAR(50) DEFAULT '' COMMENT '作者',
    view_count INT DEFAULT 0 COMMENT '浏览量',
    status TINYINT DEFAULT 1 COMMENT '状态: 0-草稿, 1-发布',
    is_top TINYINT DEFAULT 0 COMMENT '是否置顶: 0-否, 1-是',
    publish_time DATETIME COMMENT '发布时间',
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    update_time DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
    FOREIGN KEY (category_id) REFERENCES news_categories(id)
) COMMENT '新闻表';

-- 用户表
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT '用户ID',
    username VARCHAR(50) NOT NULL UNIQUE COMMENT '用户名',
    password VARCHAR(200) NOT NULL COMMENT '密码',
    nickname VARCHAR(50) DEFAULT '' COMMENT '昵称',
    avatar VARCHAR(500) DEFAULT '' COMMENT '头像',
    role TINYINT DEFAULT 0 COMMENT '角色: 0-普通, 1-admin',
    status TINYINT DEFAULT 1 COMMENT '状态: 0-禁用, 1-正常',
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    update_time DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间'
) COMMENT '用户表';

-- AI聊天表
CREATE TABLE IF NOT EXISTS aichat (
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT '聊天ID',
    user_id INT NOT NULL COMMENT '用户ID',
    role VARCHAR(20) NOT NULL DEFAULT 'user' COMMENT '角色: user/assistant',
    content TEXT NOT NULL COMMENT '消息内容',
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    FOREIGN KEY (user_id) REFERENCES users(id)
) COMMENT 'AI聊天记录表';

-- 收藏表
CREATE TABLE IF NOT EXISTS favorite (
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT '收藏ID',
    user_id INT NOT NULL COMMENT '用户ID',
    news_id INT NOT NULL COMMENT '新闻ID',
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT '收藏时间',
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (news_id) REFERENCES news(id),
    UNIQUE KEY uk_user_news (user_id, news_id)
) COMMENT '新闻收藏表';

-- 新闻刷新历史表
CREATE TABLE IF NOT EXISTS reload_history (
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT '记录ID',
    category_id INT DEFAULT NULL COMMENT '刷新分类ID',
    source VARCHAR(100) DEFAULT '' COMMENT '数据来源',
    news_count INT DEFAULT 0 COMMENT '刷新条数',
    status TINYINT DEFAULT 1 COMMENT '状态: 0-失败, 1-成功',
    message VARCHAR(500) DEFAULT '' COMMENT '备注',
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT '刷新时间',
    FOREIGN KEY (category_id) REFERENCES news_categories(id)
) COMMENT '新闻刷新历史表';

-- ===== 默认数据 =====

-- 默认分类
INSERT INTO news_categories (name, sort_order) VALUES
('科技', 1),
('体育', 2),
('娱乐', 3),
('财经', 4),
('教育', 5);

-- 默认admin用户 (密码: admin123, MD5)
INSERT INTO users (username, password, nickname, role) VALUES
('admin', 'e10adc3949ba59abbe56e057f20f883e', '管理员', 1);

-- 示例新闻
INSERT INTO news (category_id, title, summary, content, source, author, view_count, publish_time) VALUES
(2, 'GPT-5发布：AI能力再次飞跃', 'OpenAI发布GPT-5，多项能力大幅提升...', 'OpenAI今日发布了其最新一代大语言模型GPT-5，在推理、代码生成和多模态理解方面均有显著提升。', '科技日报', '张明', 1520, NOW()),
(2, '苹果Vision Pro销量突破百万', '苹果MR头显销量达新里程碑...', '苹果CEO库克表示，Vision Pro全球销量已突破100万台。', '财经网', '李华', 890, NOW()),
(3, '欧冠：皇马第15次夺冠', '皇马在欧冠决赛击败对手捧杯...', '在欧洲冠军联赛决赛中，皇家马德里以3-1战胜对手，第15次夺冠。', '体育周刊', '王磊', 2300, NOW()),
(3, '湖人晋级NBA总决赛', '湖人西部决赛4-2取胜晋级...', '洛杉矶湖人在西部决赛第六场中击败对手，成功晋级总决赛。', 'NBA中文网', '赵鑫', 1800, NOW()),
(4, '周杰伦2026巡演官宣', '周杰伦将在全国10城开唱...', '周杰伦通过社交媒体宣布2026年巡回演唱会计划，覆盖北京、上海、广州等城市。', '娱乐前线', '陈思', 5000, NOW());