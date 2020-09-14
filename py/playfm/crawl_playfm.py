#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from gevent import monkey

monkey.patch_all()

import pymongo
import requests
import traceback
from bs4 import BeautifulSoup
from queue import Empty as QueueEmpty, Queue

# urllib3.disable_warnings()

topics = ['Accounting', 'Accounting Education', 'Acoustic', 'Activism', 'Activism Roundup', 'Adventist',
          'African American', 'After Life', 'Agile', 'Agriculture', 'Agriculture Roundup', 'Alcatraz', 'Alternative',
          'Alternative Health', 'Alternative Health Roundup', 'Alternative Spirituality', "Alzheimer's Disease",
          'American Football', 'American Football Roundup', 'American Horror Story', 'American Idol', 'Anatomy',
          'Anatomy Education', 'Android', 'Angels', 'Anglican', 'Animal Rights', 'Animals and Pets', 'Animated Fiction',
          'Animation', 'Anime', 'Anthropology', 'Anthropology Education', 'Apostolic', 'App Business',
          'App Business Education', 'Apple', 'Arcade Games', 'Archaeology', 'Archaeology Education', 'Architecture',
          'Architecture Education', 'Arkansas Razorbacks', 'Arrow', 'Arsenal Football Club', 'Artificial Intelligence',
          'Arts', 'Arts Roundup', 'Astrology', 'Astronomy', 'Astronomy Education', 'Atheism', 'Audio Theater',
          'Audiobooks', 'Aussie Rules', 'Authors', 'Autism', 'Auto', 'Avatar - The Last Airbender', 'Aviation', 'Bands',
          'Baptist', 'Baseball', 'Baseball Roundup', 'Basketball', 'Basketball Roundup', 'Batman',
          'Battlestar Galactica', 'Bedtime Stories', 'Beekeeping', 'Beer', 'Being Human', 'Better Call Saul',
          'Bible Prophecy', 'Big Brother', 'Bigfoot', 'Biology', 'Biology Education', 'Biotech', 'Birds', 'Blogging',
          'Blues', 'Bodybuilding', 'Bollywood', 'Books', 'Books and Writing', 'Boxing', 'Breaking Bad', 'Breaking News',
          'Brethren', 'Buddhist', 'Buffy the Vampire Slayer', 'Business', 'Business Disciplines', 'Business Education',
          'Business English', 'Business News', 'Business Trends', 'Cardiology', 'Careers', 'Castle', 'Catechesis',
          'Catholic', 'Cats', 'Chemistry', 'Chemistry Education', 'Chess', 'Chicago Cubs', 'Chiropractic', 'Christian',
          'Christian Apologetics', 'Christian Orthodox', 'Christian Students', 'Christianity', 'Cinema',
          'Cinema Roundup', 'Classic Radio', 'Classic Sitcoms', 'Classic TV', 'Classic TV Roundup', 'Classical',
          'Clean Comedy', 'Climate Change', 'Climbing', 'Cloud IT', 'Cloud IT Education', 'Coaching', 'Combat Sports',
          'Comedian Chat', 'Comedian Interviews', 'Comedy', 'Comics', 'Comics Roundup', 'Communities',
          'Community Church', 'Computer Science', 'Conservative', 'Conspiracy Theories', 'Conversations',
          'Cosmetic Surgery', 'Country', 'Creativity', 'Cricket', 'Crime', 'Cruising', 'Current Affairs', 'Current TV',
          'Cyber Currency', 'Cycling', 'DC', 'Daily Business News', 'Daily News', 'Daily Tech News', 'Dark Souls',
          'Darts', 'Data Science', 'Dating', 'Dentistry', 'Desperate Housewives', 'Destiny', 'DevOps', 'Dexter',
          'Diabetes', 'Digital Marketing', 'Disc Golf', 'Disney', 'Do It Yourself', 'Doctor Who', 'Documentaries',
          'Dogs', 'Dollhouse', 'DotA', 'Downton Abbey', 'Dragnet', 'Drama', 'Drones', 'Drum and Bass', 'Drupal',
          'Dungeons and Dragons', 'E-Commerce', 'E-Commerce Education', 'Eclectic', 'Economics', 'Education',
          'Education Tech', 'Electronic', 'Elite: Dangerous', 'Elvis Presley', 'Emergency Medicine', 'Endurance Sports',
          'Energy', 'Engineering', 'English Pronunciation', 'English Usage', 'Entertainment', 'Entertainment Industry',
          'Entrepreneur', 'Entrepreneur Interviews', 'Entrepreneur Lifestyle', 'Entrepreneur Roundup', 'Environment',
          'Environment Roundup', 'Equestrian', 'Evangelical', 'F1', 'Facts and Trivia', 'Falling Skies', 'Family',
          'Fantasy', 'Fantasy American Football', 'Fantasy Aussie Rules', 'Fantasy Baseball', 'Fantasy Basketball',
          'Fantasy Hockey', 'Fantasy Soccer', 'Fantasy Sports', 'Fantasy Sports Roundup', 'Fascinating People',
          'Fashion and Beauty', 'Fatherhood', 'Fellowship', 'Female Pop Singers', 'Feminist', 'Filmmaking',
          'Final Fantasy', 'Finance', 'Fine Arts', 'Firefly', 'Fish', 'Fishing', 'Fitness', 'Fitness Industry',
          'Fitness Roundup', 'Folk', 'Food', 'Food and Beverage', 'Football Manager', 'Freelancing', 'Fringe',
          'Future Trends', 'Gadgets', 'Gambling', 'Game Development', 'Game of Thrones', 'Games and Gambling',
          'Gardening', 'Geekery', 'Genealogy', 'Genetics', 'Geocaching', 'Geography', 'Geology', 'Geology Education',
          'Gilmore Girls', 'Glee', 'Go To Sleep', 'Golf', 'Gospel Music', 'Gossip Girl', 'Gotham', 'Graphic Design',
          'Green Lantern', 'Greentech', "Grey's Anatomy", 'Guitar', 'Gunsmoke', 'Harry Potter', 'Health Care',
          'Health Industry', 'Health News', 'Health and Well-Being', 'Hearthstone', 'Heroes of the Storm',
          'Higher Education', 'Hindu', 'Hiphop', 'History', 'Hobbies', 'Hockey', 'Hockey Roundup', 'Holistic Health',
          'Homeland', 'Homeschooling', 'Horror', 'Horror Roundup', 'Horror Stories', 'Horseracing', 'House of Cards',
          'Human Resources', 'Human Rights', 'Humanities Education', 'Humor', 'Hunger Games', 'Hunting', 'Hypnosis',
          'IT Industry', 'IT Management', 'Immunology', 'Improv', 'Inclusive Education', 'Indie Music', 'Industries',
          'Intellectual Property', 'Interior Design', 'International News', 'International Relations', 'Islamic',
          'J-pop', 'J.R.R. Tolkien', 'James Bond', 'Java', 'Jazz', 'Jewish', 'Journalism', 'Justified', 'K-pop',
          'Kids and Family', 'Knitting', 'LGBT', 'Language Learning', 'Last Resort', 'Latin Music', 'Law',
          'Law Roundup', 'Leadership', 'League of Legends', 'Learning Arabic', 'Learning Chinese', 'Learning English',
          'Learning English Roundup', 'Learning French', 'Learning German', 'Learning Hindi', 'Learning Italian',
          'Learning Japanese', 'Learning Korean', 'Learning Portuguese', 'Learning Russian', 'Learning Spanish',
          'Libertarian', 'Lifestyle', 'Linguistics', 'Linguistics Education', 'Linux', 'Linux Education', 'Liquor',
          'Liverpool Football Club', 'Lord of the Rings', 'Lost', 'Lutheran', 'MBA', 'MBA Education', 'MMA', 'MS Dev',
          'Mad Men', 'Magic: The Gathering', 'Manchester City Football Club', 'Marathon', 'Marketing',
          'Marketing Education', 'Marketing Roundup', 'Marriage', 'Martial Arts', 'Marvel', 'Math', 'Math Education',
          'Mature Comedy', 'Media', 'Medicine', 'Medicine Roundup', 'Meditation', "Men's Corner",
          "Men's Corner Roundup", "Men's Health", 'Mental Health', 'Mental Health Roundup', 'Metal', 'Metaphysics',
          'Meteorology', 'Methodist', 'Michael Jackson', 'Michigan Wolverines', 'Military', 'Military History',
          'Minecraft', 'Modern Family', 'Money', 'Mormon', 'Motherhood', 'Motorcycle', 'Motorsports',
          'Motorsports Roundup', 'Music', 'Music Business', 'Music Industry', 'Musicality', 'Musicians', 'Mystery',
          'Mythology', 'NASCAR', 'NBA', 'NBA Roundup', 'Naruto', 'Native American', 'Natural Sciences', 'Netrunner',
          'Neurology', 'Neuroscience', 'New Age', 'New York Giants', 'News', 'News Comedy', 'News Talk',
          'News and Entertainment', 'Nintendo', 'Non-Profit', 'Nutrition', 'Nutrition Roundup', 'Oceanography',
          'Oklahoma City Thunder', 'Oldies', 'Once Upon a Time', 'Oncology', 'Open Source', 'Operating Systems',
          'Ophthalmology', 'Oracle', 'Outdoor', 'PC Gaming', 'Paganism', 'Painting', 'Paleo', 'Paleontology',
          'Paranormal', 'Parenting', 'Pentecostal', 'Period Drama', 'Permaculture', 'Personal Finances', 'Pets',
          'Pharmacology', 'Philosophy', 'Photography', 'Physical Therapy', 'Physics', 'Piano', 'Pilates', 'Pinball',
          'Pixar', 'PlayStation', 'Podcasting', 'Podcasting Education', 'Poetry', 'Poetry Reading', 'Pokemon', 'Poker',
          'Political Comedy', 'Political Drama', 'Political Science', 'Politics', 'Politics Roundup', 'Pop',
          'Pop Culture', 'Poultry', 'Power Rangers', 'Presbyterian', 'Pretty Little Liars', 'Pro Wrestling',
          'Productivity', 'Prog Languages', 'Programming', 'Programming Education', 'Progressive', 'Project Management',
          'Protestant', 'Psychiatry', 'Psychic', 'Psychology', 'Psychology Education', 'Public Relations', 'Publishing',
          'Publishing Education', 'Qigong And Tai Chi', 'Quilting', 'Real Estate', 'Real Estate Education',
          'Reality TV', 'Reality TV Roundup', 'Recent TV', 'Reggae', 'Reiki', 'Relationship', 'Relationship Roundup',
          'Religion', 'Religion Roundup', 'Retro', 'Retro Gaming', 'Revolution', 'Rock', 'Rocky', 'Romance', 'Ruby',
          'Rugby', 'RuneScape', 'Running', 'SEO', 'SEO Education', 'Sailing', 'Sailormoon', 'Sales', 'Salvation Army',
          'Scandal', 'School Education', 'Sci-Fi', 'Sci-Fi / Fantasy Stories', 'Sci-Fi Roundup', 'Science',
          'Science Education', 'Science Roundup', 'Screenwriting', 'Secret Circle', 'Security', 'Self-Help',
          'Self-Improvement', 'Serial', 'Sexuality', 'Shakespeare', 'Shamanism', 'Sherlock Holmes', 'Short Stories',
          'Showbiz', 'Skeptic', 'Sketch Comedy', 'Sleepy Hollow', 'Smallville', 'Soap Opera', 'Soccer',
          'Soccer Roundup', 'Social Media', 'Social Media Education', 'Social Sciences', 'Society', 'Sociology',
          'Sociology Education', 'Software Development', 'Soul', 'Soundtrack', 'South America', 'South Park',
          'Spartacus', 'Specialized News', 'Spiritual Beings', 'Sports', 'Sports Betting', 'Sports Medicine',
          'Sports News', 'Sports and Entertainment', 'Spy', 'Stand-up Comedy', 'Star Trek', 'Star Wars', 'Stargate',
          'Storytelling', 'Strength Training', 'Superheroes', 'Superman', 'Supernatural', 'Survivor', 'Swimming',
          'Sysadmin', 'TV', 'TV Roundup', 'Table Top Games', 'Table Top Games Roundup', 'Tarot', 'Taxation', 'Teaching',
          'Teaching Trends', 'Tech', 'Tech Education', 'Tech News', 'Tech Startups', 'Tech Tips', 'Tennis',
          'Terra Nova', 'The Americans', 'The Bachelor', 'The Beatles', 'The Blacklist', 'The Elder Scrolls',
          'The Flash', 'The Following', 'The Newsroom', 'The Real Housewives', 'The Simpsons', 'The Strain',
          'The Twilight Zone', 'The West Wing', 'The Young and the Restless', 'Theater', 'Theme Parks', 'Theology',
          'Toronto Blue Jays', 'Toronto Maple Leafs', 'Tottenham Hotspur Football Club', 'Toys', 'Trading',
          'Transformers', 'Travel', 'Travel Roundup', 'Triathlon', 'True Blood', 'True Crime', 'True Crime Roundup',
          'True Detective', 'True Stories', 'Twilight', 'UFOs', 'UK Politics', 'US Government', 'US Military',
          'US Military Family', 'US Veterans', 'Ukulele', 'Unitarian Universalist', 'Urban Survival', 'User Experience',
          'Vampire Diaries', 'Varsity Teams', 'Vegan', 'Venture Capital', 'Video Game Music', 'Video Games',
          'Video Games Roundup', 'Walking Dead', 'Warhammer', 'Washington Redskins', 'Weather Alerts',
          'Web Development', 'Web Development Education', 'Weightlifting', 'Westworld', 'Whiskey', 'Windows', 'Wine',
          "Women's Corner", "Women's Corner Roundup", "Women's Health", 'Woodworking', 'Wordpress', 'World of Warcraft',
          'Worldbuilding', 'Writing', 'X Factor', 'X-Files', 'Xbox', 'Yoga']

client = pymongo.MongoClient()
db = client['playfm']
cache_table = db['cache']
cache_table_page = db['cache_page']


def get_cache_data(key):
    r = cache_table.find_one({'_id': key}) or {}
    return r.get('data')


def set_cache_data(key, data):
    cache_table.update_one({'_id': key}, {'$set': {'data': data}}, upsert=True)


def get_cache_links(key, page=False):
    table = cache_table_page if page else cache_table
    r = table.find_one({'_id': key}) or {}
    return r.get('links')


def set_cache_links(key, links, page=False):
    table = cache_table_page if page else cache_table
    table.update_one({'_id': key}, {'$set': {'links': links}}, upsert=True)


seen = set()

Q = Queue()


def worker():
    while not Q.empty():
        try:
            url = Q.get_nowait()
        except QueueEmpty:
            continue
        try:
            links = visit_url(url)
        except Exception as e:
            links = []
            print('exception occusrs when fetching url. url = %s' % url)
            traceback.print_exc()
        for link in links:
            Q.put(link)
    print('Q is empty. quit.')


def visit_url(url):
    if url in seen:
        return []

    seen.add(url)

    def is_follow_url(x):
        if not (x.startswith('/series/') or x.startswith('/podcasts/')):
            return False
        if x.startswith('/series/') and len(x.split('/')) != 3:
            return False
        return True

    def make_follow_url(x):
        if x.startswith('/series/'):
            return 'https://player.fm' + x
        else:
            return 'https://player.fm/mu' + x

    # 翻页数据只记录links, 非翻页数据保存links和data.
    def get_url_links(url, page=False):
        links = get_cache_links(url, page)
        if links is None:
            r = requests.get(url)
            data = r.content
            bs = BeautifulSoup(data, "lxml")
            links = [x.attrs.get('href', '') for x in bs.findAll('a')]
            links = [x for x in links if is_follow_url(x)]
            if not page:
                set_cache_data(url, data)
            set_cache_links(url, links, page)
        return links

    url = make_follow_url(url)
    print('visit url = %s' % url)
    links = get_url_links(url)

    # 处理翻页问题
    if url.find('/series/') == -1:
        offset = 0
        limit = 50
        while True:
            actual_url = url + '/series?active=true&limit=%d&order=popular&container=false&offset=%d' % (limit, offset)
            print(actual_url)
            sub_links = get_url_links(actual_url, page=True)
            if not sub_links:
                print('BREAK AT %d!!!' % offset)
                break
            if offset >= 1000:
                print('WARNING URL = %s' % actual_url)
                break
            offset += 50
            links.extend(sub_links)
    links = list(set(links))
    return links


def main():
    # seed urls.
    for t in topics:
        t = t.replace("'", '').replace(' ', '-').lower()
        url = '/featured/' + t
        Q.put(url)

    n_threads = 10
    from gevent.pool import Pool as ThreadPoolExecutor

    pool = ThreadPoolExecutor()
    for i in range(n_threads):
        pool.spawn(worker)
    pool.join()
    print('main quit')


if __name__ == '__main__':
    main()
