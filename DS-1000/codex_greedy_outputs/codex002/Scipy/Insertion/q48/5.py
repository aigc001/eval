
result = stats.ranksums(pre_course_scores, during_course_scores)
pvalue = result.pvalue
print(pvalue)
