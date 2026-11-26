
# Student Feedback Sentiment Scoring

positive_words = ["good", "excellent", "helpful", "nice", "best"]
negative_words = ["bad", "poor", "boring", "difficult", "worst"]

feedback = input("Enter student feedback: ").lower()

positive = 0
negative = 0

words = feedback.split()

for word in words:

    if word in positive_words:
        positive += 1

    elif word in negative_words:
        negative += 1

score = positive - negative

print("\n--- Feedback Analysis ---")
print("Positive Words:", positive)
print("Negative Words:", negative)
print("Sentiment Score:", score)

if score > 0:
    print("Feedback: Positive")

elif score < 0:
    print("Feedback: Negative")

else:
    print("Feedback: Neutral")
