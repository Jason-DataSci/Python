import pandas as pd
data = pd.DataFrame(columns=('video_title', 'video_img', 'video_id', 'video_length', 'video_review', 'video_genres'))

class Pandas:

    @classmethod
    def concat(cls, video_title, video_img, video_id, video_length, video_review, video_genres):
        page = pd.DataFrame({
            'video_title': [video_title],
            'video_img': [video_img],
            'video_id': [video_id],
            'video_length': [video_length],
            'video_review': [video_review],
            'video_genres': [video_genres]})
        data = data.append(page, ignore_index=True)
