from nltk.tokenize import sent_tokenize
rd="""Willing to take on any task to help team. Reliable and dedicated
team player with hardworking and resourceful approach. To
pursue a challenging career and be a part of progressive
organization that gives a scope to enhance my knowledge and
utilizing my skills towards the growth of the organization"""
rd=sent_tokenize(rd)
print(rd)
print(type(rd))