# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

class JavlibPipeline(object):
        def open_spider(self, spider):
            self.conn = sqlite3.connect('javlib.db')
            self.cur = self.conn.cursor()
            self.cur.execute('create table if not exists javlib (video_title varchar, video_img varchar, video_id varchar, video_length varchar, video_review varchar, video_genres varchar, video_cast varchar)')
            # pass

        def close_spider(self, spider):
            self.conn.commit()
            self.conn.close()
            # pass

        def process_item(self, item, spider):
            col = ','.join(item.keys())
            placeholders = ','.join(len(item) * '?')
            sql = 'insert into javlib({}) values({})'
            self.cur.execute(sql.format(col, placeholders), item.values())
            return item
