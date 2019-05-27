# Predicting New r/AskReddit Posts' Popularity

I have one question I want to answer. Out of the hundreds of submissions r/AskReddit gets every day, is there a way to tell which ones will make it to the top of the subreddit? 

I can't think of a real, practical use for this. It is true that the earlier you comment in a successful thread, the more likely you are to get a comment with a lot of karma. If your comment is one of the top ones early on, it will keep gathering upvotes as the post gets more popular and more and more people see the comments. 

This prediction task seems hard for a couple of reasons. 

1. There probably aren't a lot of people visiting the New section of a subreddit at any given moment, so you will get a lot of variability in what kinds of posts get upvotes at any given point. I've seen a lot of posts of Redditors complaining about a piece of original content they submitted that didn't garner much attention, but later on some one took their submission, reposted it, and made it to the front page.
2. Automatically rating how good of a question an r/AskReddit submission is sounds like a nightmare. I don't know anything about NLP, and barely anything about RNNs. On the plus side, this will give me exposure to the techniques used in that field. It would have been helpful to be familiar with some of those techniques for that Two Sigma Kaggle competition about prediction equities movement from news data. The downside is that learning new techniques takes a long time and doesn't have a clear path to success, which are bad news for a short project because it increases the chance of it never getting done.
3. People's tastes can change and performance is context dependent. The lifecycle of a good meme format is probably around a month. If I train a model with data from a small subset of time, what's to say that the model won't capture something about that specific trend that will become useless in not that long of a time? It also matters how saturated the subreddit has been with similar questions. One original, funny, thought provoking question could make it to the top of the front page one day, but post it next week and it will most likely not get the same traction because no one wants to the same thing asked again (I have seen some questions repeated and still be successful in the subsequent posts, but there is a refractory period during which submitting the same post won't get traction).

I do have a hunch that if someone were to go through the new submissions, they'd be able to tell which posts will make it to the top at a better rate than a random classifier. It seems very likely that someone will also be very good at telling which posts will definitely *not* make it to the front page. From my own experience going through new, most posts are badly phrased, don't make sense, ask questions that are not conducive to discussion, etc.

I think that a successful project would produce a model with a very low false negative rate, and not-so-high false positive rate. The goal would be to select the posts which could possibly make it, while correctly discarding the posts that definitely have no chance of making it.

