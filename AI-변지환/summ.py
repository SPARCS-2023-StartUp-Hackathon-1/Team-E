import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Load the model and tokenizer
model = AutoModelForSeq2SeqLM.from_pretrained("philschmid/bart-large-cnn-samsum")
tokenizer = AutoTokenizer.from_pretrained("philschmid/bart-large-cnn-samsum")

# Define your input text
input_text = """Noah Cyrus just earned the title of breast dressed at Paris Fashion Week.

The "July" singer wasn't afraid to free the nipple during an afternoon outing in the City of Light, as she stepped out in a black chest-baring gown on Jan. 24. Noah's Stéphane Rolland Haute Couture design featured a large chain-link attachment that barely covered her breasts and an even more plunging neckline that swooped just above her belly button.

The 23-year-old's head-turning dress, which looked like something out of Morticia Addams' glamorously macabre closet, also included long sleeves and a floor-length train for a mini dose of modesty. She paired her outfit with sheer pantyhose, black strappy heels and bleached eyebrows.

This wasn't Noah's only fierce style moment this week.

For the Marine Serre show on Jan. 21, she rocked a bold catsuit with the brand's famous half-moon pattern and layered a baroque-printed bodysuit on top. During Alexandre Vauthier's Jan. 24 presentation, Noah donned a sparkly bikini that she wore underneath a completely see-through pleated gown."""

input_text = input_text.replace("\n", " ")

# Encode the input text
input_ids = tokenizer.encode(input_text, return_tensors='pt')

# Generate summary
summary_ids = model.generate(input_ids, num_beams=3, min_length = 56,early_stopping=True)

# Decode the summary
summary_text = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

# Print the summary
print(summary_text)

"""보다 합리적인 요약을 생성하기 위해 제공한 코드의 하이퍼 파라미터를 조정하는 몇 가지 방법이 있습니다. 다음은 몇 가지 예입니다:

num_numbers: num_beams 매개 변수는 빔 검색 알고리즘에 사용되는 빔의 수를 결정합니다. 빔 수를 늘리면 요약 집합이 더 다양해질 수 있지만 계산 시간도 늘어날 수 있습니다. 빔 수를 줄이면 계산 시간이 빨라지지만 요약의 다양성은 떨어질 수 있습니다. 이 매개 변수의 적절한 값은 2와 6 사이입니다.

max_length: max_length 매개 변수는 요약의 최대 토큰 수를 지정하는 데 사용됩니다. 매개 변수를 너무 높게 설정하면 모델이 너무 긴 요약을 생성하고 너무 낮게 설정하면 모델이 전체 요약을 생성하지 못할 수 있습니다. 이 매개 변수의 적절한 값은 입력 텍스트의 길이에 따라 50에서 100 사이입니다.

min_length: min_length 매개 변수는 요약의 최소 토큰 수를 지정하는 데 사용됩니다. 매개 변수를 너무 높게 설정하면 모형에서 너무 짧은 요약을 생성하지 않고 너무 낮게 설정하면 모형에서 너무 불완전한 요약을 생성할 수 있습니다. 이 매개 변수의 적절한 값은 입력 텍스트의 길이에 따라 30-60 사이입니다.

early_filename: early_stopping 매개 변수는 모델이 충분히 좋은 요약을 생성한 경우 생성 프로세스를 중지하는 데 사용됩니다. 이렇게 하면 생성 프로세스의 속도를 높이는 데 도움이 될 수 있지만 너무 적극적으로 설정하면 모형이 최상의 요약을 생성하지 못할 수 있습니다. 이 매개 변수에 대한 적절한 값은 True입니다.

no_repeat_ngram_size : 기본적으로 no_repeat_ngram_size 매개 변수는 3으로 설정됩니다. 즉, 모델은 요약에서 이미 생성된 n-gram(여기서 n은 매개 변수의 값)을 생성하지 않습니다. 이렇게 하면 요약에서 반복을 방지하는 데 도움이 되지만 매개 변수가 너무 높게 설정되어 있으면 모형이 전체 요약을 생성하지 못할 수 있습니다. 이 매개 변수의 적절한 값은 2와 4 사이입니다.

하이퍼 파라미터 설정의 최선의 선택은 특정 작업과 입력 데이터에 따라 달라지므로 항상 다른 설정으로 실험하고 결과를 평가하는 것이 좋습니다."""