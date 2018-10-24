class Queries(object):
    def __init__(self):
        self.GET_ALL_CHINEESE = """ select from Chinese """
        self.GET_ALL_ORIGINS_FROM_THEME = "select list(in.name) as origin from relate where out.@class = 'Theme' and out.name = '{0}'"
        self.FIND_BY_ORIGINAL = """select outE('RelateTranslation').in.name as translation, 
                                outE('RelateTranscription').in.name as transcription from 
                                Chinese where name = '{0}'"""
        self.GET_THEME = """
            select out.name as theme from Relate where in.@class = 'Chinese' and in.name in {0}
            """
