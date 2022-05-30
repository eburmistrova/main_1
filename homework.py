import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

talks = pd.read_csv('TED Talks.csv')
talks_group= talks.groupby('author')

authors = []
views = []
likes = []

for name, group in talks_group:
    if len(group) > 5:
        # print(name, len(group))
        # print(group)
        mean = group[['views','likes']].mean()
        # print('views: %.2f' % mean['views'])
        # print('likes: %.2f' % mean['likes'])
        authors.append(name)
        views.append(mean['views'])
        likes.append(mean['likes'])

for i in range(0, len(authors)):
    print(authors[i], views[i], likes[i])


plt.figure(figsize=(10, 10))    
    
plt.subplot(2,1,1)
index = np.arange(len(authors))
plt.axis([0, max(views), 0, len(authors)])
plt.title('Кол-во просмотров')
plt.barh(index, views, 0.5)
plt.yticks(index, authors)


plt.subplot(2,1,2)
index = np.arange(len(authors))
plt.axis([0, max(likes), 0, len(authors)])
plt.title('Кол-во лайков')
plt.barh(index, likes, 0.5)
plt.yticks(index, authors)
plt.show()
