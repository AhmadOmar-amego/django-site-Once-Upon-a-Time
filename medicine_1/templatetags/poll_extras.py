from django import template
# from ..merge_nlp import all_nlp,all_nlp_2
from ..rev_extract import all_rev
from collections import defaultdict
from ..all_with_topic import all_rev_with
from ..ml import all_ml
register = template.Library()
import  pandas as pd

@register.filter(name='jump_link')

def jump_link(context):
    rev = []
    rev.append(context)
    p =all_rev_with(rev)
    print("pppppppp")
    # p= defaultdict(p)

    pred=all_ml(p)
    print("preddddddddddd" ,  pred)

    percentile_list = pd.DataFrame(p)
    percentile_list.columns = ["review", "topic"]
    percentile_list['classo'] = pd.Series(pred, index=percentile_list.index)
    for p in percentile_list.values:
          if 0 in percentile_list.classo.values:
            # Book_Info
            print("in anything")
            if p[1] == 'Book_Info':
                print("in first if")
                Book_Info = percentile_list[(percentile_list.topic == "Book_Info")]
                if p[2]==1:
                    print("in 1 if")
                    #             Book_Info=percentile_list[(percentile_list.topic == "Book_Info")  ]
                    justone_Book = (Book_Info[(Book_Info.classo == 1)].classo.value_counts()).astype('float').values
                    Book_info_count = Book_Info.topic.value_counts().astype('float').values
                    percent_Book = (justone_Book / Book_info_count) * 100
                    return ("negativty for  book", percent_Book[0], "%")
                else:
                    print("in 2 if")
                    #             Book_Info=percentile_list[(percentile_list.topic == "Book_Info")  ]
                    justone_Book = (Book_Info[(Book_Info.classo == 0)].classo.value_counts()).astype('float').values
                    Book_info_count = Book_Info.topic.value_counts().astype('float').values
                    percent_Book = (justone_Book / Book_info_count) * 100
                    return("positivty for book", percent_Book[0], "%")
    return ("book No information")
      #   #  else:
      #     #     print("bla")
      #     #     return("the people who talk about book none")
      #       if p[1] == 'content':
      #           content = percentile_list[(percentile_list.topic == "content")]
      #           if p[2] == 1:
      #               #             content=percentile_list[(percentile_list.topic == "content")  ]
      #               justone_content = (content[(content.classo == 1)].classo.value_counts()).astype('float').values
      #               content_count = content.topic.value_counts().astype('float').values
      #               percent_content = (justone_content / content_count) * 100
      #               return ("the people who hated content", percent_content[0], "%")
      #           else:
      #               content = percentile_list[(percentile_list.topic == "content")]
      #               justone_content = (content[(content.classo == 0)].classo.value_counts()).astype('float').values
      #               content_count = content.topic.value_counts().astype('float').values
      #               percent_content = (justone_content / content_count) * 100
      #               return ("the people who loved content", percent_content[0], "%")
      #       #else:
      # #          return ("the people who talk about content none")
      #           # story_twist
      #       if p[1] ==  'story_twist':
      #           story_twist = percentile_list[(percentile_list.topic == "story_twist")]
      #           if p[2] == 1:
      #
      #               justone_story_twist = (story_twist[(story_twist.classo == 1)].classo.value_counts()).astype(
      #                   'float').values
      #               story_twist_count = story_twist.topic.value_counts().astype('float').values
      #               percent_story_twist = (justone_story_twist / story_twist_count) * 100
      #               return ("the people who hated story_twist", percent_story_twist[0], "%")
      #           else:
      #               story_twist = percentile_list[(percentile_list.topic == "story_twist")]
      #               justone_story_twist = (story_twist[(story_twist.classo == 0)].classo.value_counts()).astype(
      #                   'float').values
      #               story_twist_count = story_twist.topic.value_counts().astype('float').values
      #               percent_story_twist = (justone_story_twist / story_twist_count) * 100
      #               return ("the people who loved story_twist", percent_story_twist[0], "%")
      #
      #   #    else:
      #   #        return ("the people who talk about story_twist none")
      #           # character
      #       if p[1] ==  'character': #in percentile_list.values:
      #           character = percentile_list[(percentile_list.topic == "character")]
      #           if p[2] == 1:# in character.classo.values:
      #
      #               print("CHAR 1")
      #               justone_character = (character[(character.classo == 1)].classo.value_counts()).astype('float').values
      #               character_count = character.topic.value_counts().astype('float').values
      #               percent_character = (justone_character / character_count) * 100
      #               return ("the people who hated character", percent_character[0], "%")
      #           else:
      #               print("CHAR 2")
      #               character = percentile_list[(percentile_list.topic == "character")]
      #               justone_character = (character[(character.classo == 0)].classo.value_counts()).astype('float').values
      #               character_count = character.topic.value_counts().astype('float').values
      #               percent_character = (justone_character / character_count) * 100
      #               return ("the people who loved character", percent_character[0], "%")
      #       else:
      #           return ("the people who talk about character none")
      #       # content


@register.filter(name='jump_link_2')
def jump_link_2(context):
    rev = []
    rev.append(context)
    p =all_rev_with(rev)
    pred=all_ml(p)
    percentile_list = pd.DataFrame(p)
    percentile_list.columns = ["review", "topic"]
    percentile_list['classo'] = pd.Series(pred, index=percentile_list.index)
    for p in percentile_list.values:
        if 0 in percentile_list.classo.values:
            # Book_Info
            print("chare" , p[1] , p[2])
            if p[1] ==  'character': #in percentile_list.values:
                character = percentile_list[(percentile_list.topic == "character")]
                if p[2] == 1:# in character.classo.values:

                    print("CHAR 1")
                    justone_character = (character[(character.classo == 1)].classo.value_counts()).astype('float').values
                    character_count = character.topic.value_counts().astype('float').values
                    percent_character = (justone_character / character_count) * 100
                    return ("negativty for character", percent_character[0], "%")
                else:
                    print("CHAR 2")
                    character = percentile_list[(percentile_list.topic == "character")]
                    justone_character = (character[(character.classo == 0)].classo.value_counts()).astype('float').values
                    character_count = character.topic.value_counts().astype('float').values
                    percent_character = (justone_character / character_count) * 100
                    return ("positivty for  character", percent_character[0], "%")
    return ("character none")



@register.filter(name='jump_link_3')
def jump_link_3(context):
    rev = []
    rev.append(context)
    p =all_rev_with(rev)
    pred=all_ml(p)
    percentile_list = pd.DataFrame(p)
    percentile_list.columns = ["review", "topic"]
    percentile_list['classo'] = pd.Series(pred, index=percentile_list.index)
    for p in percentile_list.values:
        if p[1] == 'story_twist':
            story_twist = percentile_list[(percentile_list.topic == "story_twist")]
            if p[2] == 1:

                justone_story_twist = (story_twist[(story_twist.classo == 1)].classo.value_counts()).astype(
                    'float').values
                story_twist_count = story_twist.topic.value_counts().astype('float').values
                percent_story_twist = (justone_story_twist / story_twist_count) * 100
                return ("negativty for story_twist", percent_story_twist[0], "%")
            else:
                story_twist = percentile_list[(percentile_list.topic == "story_twist")]
                justone_story_twist = (story_twist[(story_twist.classo == 0)].classo.value_counts()).astype(
                    'float').values
                story_twist_count = story_twist.topic.value_counts().astype('float').values
                percent_story_twist = (justone_story_twist / story_twist_count) * 100
                return ("positivty for story_twist", percent_story_twist[0], "%")
        return("story_twist none")



@register.filter(name='jump_link_4')
def jump_link_4(context):
    rev = []
    rev.append(context)
    p =all_rev_with(rev)
    pred=all_ml(p)
    percentile_list = pd.DataFrame(p)
    percentile_list.columns = ["review", "topic"]
    percentile_list['classo'] = pd.Series(pred, index=percentile_list.index)
    for p in percentile_list.values:

        if p[1] == 'content':
            content = percentile_list[(percentile_list.topic == "content")]
            if p[2] == 1:
                #             content=percentile_list[(percentile_list.topic == "content")  ]
                justone_content = (content[(content.classo == 1)].classo.value_counts()).astype('float').values
                content_count = content.topic.value_counts().astype('float').values
                percent_content = (justone_content / content_count) * 100
                return ("negativty for content", percent_content[0], "%")
            else:
                content = percentile_list[(percentile_list.topic == "content")]
                justone_content = (content[(content.classo == 0)].classo.value_counts()).astype('float').values
                content_count = content.topic.value_counts().astype('float').values
                percent_content = (justone_content / content_count) * 100
                return ("positivty for content", percent_content[0], "%")
    return ("content none")