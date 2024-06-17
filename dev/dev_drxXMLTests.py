## DEVELOPMENT: Test Paths
PATH_NO_EVALS = 'PyTables/tests/no_evals.xml'
PATH_0 = "PyTables/tests/small.xml"
PATH_1 = "PyTables/tests/concept.xml"
PATH_2 = "PyTables/tests/middle.xml"
PATH_3 = "PyTables/tests/final.xml"

## Library Imports
from defusedxml.ElementTree import *
import conversation

# dom = parse(PATH_0)
# comment_ids = dom.findall('./Comments/comment/id')
# print(len(comment_ids))
# for comment_id in comment_ids:
#     print(comment_id.text)

# comments = dom.findall('./Comments/comment')
# print(len(comments))
# for comment in comments:
#     # print(comment.find('./id').text)
#     # print(comment.find('./status').text)
#     # print(len(comment.find('./evaluations')))
#     try:
#         evals = comment.find('./evaluations')
#         # print(type(evals), len(evals))  # Type of evals and how many child elements, which are eval
#         for eval in evals:
#             print(eval.find('./status').text)
#     except:
#         id = comment.find('./id').text
#         print(f'{id} does not have evaluations')


# for comment in comments:
    # print(comment.find('./id').text)
    # aComment = conversation.Comment(comment)
    # print(aComment.id)
    # print(aComment.comment_text)
    # print(aComment.properties['id'])

# aComment = conversation.Comment(comments[0])
# aComment.print_all()
# aComment.print_single('attachment')

# print(aComment.evals.find('./id').text)

# print(len(aComment.backchecks))
# print(aComment.evaluation_count)
# print(aComment.backcheck_count)

# print(aComment.properties['evaluations'][1].find('./id').text)

# for eval in aComment.properties['evaluations']:
#     print(eval.find('./id').text)
#     print(eval.find('./evaluationText').text)


# print(aComment.properties['evaluations'])
# print(aComment.evaluations_count, aComment.backchecks_count)

# for eval in aComment.properties['evaluations']:
#     print(eval.properties)


# eval = aComment.properties['evaluations'][0]
# print(eval.to_string())

# for prop in eval.properties:
#     print(prop + ":", eval.properties[prop])

# eval.print_all()
# eval.print_single()
# eval.print_single('createdOn')

# print(aComment.properties)


dom = parse(PATH_0)
root = dom.getroot()
# drChecks = conversation.ProjectInfo(root.find('./DrChecks'))


# print(root.find('./DrChecks')[0].text)
# print(drChecks.properties['ProjectName'])

review = conversation.Review(root)
# review.project_info.print_all()

# review.comments[0].properties['evaluations'][1].print_all()

# print(review.comments[0].evaluations[1].hasAttachment)

for eval in review.comments[0].evaluations:
    print(eval.id, eval.hasAttachment)