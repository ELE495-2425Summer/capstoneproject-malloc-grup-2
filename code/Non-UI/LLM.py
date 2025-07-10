import openai

basla = 1

user_input =  'sağa git, 6 saniye ilerle, sola git, bir engel görene kadar ilerle sonra sola dön sonra takla at amuda kalk sonra sola git, bir engel görene kadar ilerle sonra sola dön sonra zibar yat geri dön, ileriye ilerle, 68 baba elektronlar ilerliyor sağa git sola dön maşallah oğluma' # input("Ask me something: ")

openai.api_key = ""


def ask_chatgpt(prompt, model="gpt-4o"):#ığş
    if(basla):
        system_instruction = "Gelen araç komutlarını cevabında bir komut sırasına sokmalısın,Sayıları harflerle değil rakamlar ile söyle. örneğin ‘sağa git, 2 saniye düz git, sola git, bir engel görene kadar ilerle sonra sola dön, geriye dön, sola dön ve 5 saniye geri git dediğimde, bu komutu tam olarak şu cevap sırasına dönüştürmelisiniz : '[sağa dönüyorum],[2 saniye ileri gidiyorum],[sola dönüyorum],[ileri gidiyorum],[sola dönüyorum], [geri dönüyorum],[sola dönüyorum],[2 saniye geri gidiyorum] '. Ve eğer x süre boyunca (veya bir engel görene kadar) ileriye veya geriye, sağa, sola, geri gitme veya geriye dönme içermeyen bir komut tespit ederseniz, o zaman bu komutu yapamayacağını yorumlayarak iletmelisin. Örnegin sağa git, uçarak 5 saniye ileri git, mavi renk gördüğünde saga dön, 2 saniye ileri git ve 2 saniye sonra amuda kalk gibi komutlara : [sağa dönüyorum],[ucarak gidemem],[renk tespiti yapamam],[2 saniye ileri gidiyorum],[amuda kalkamam] seklinde cevap ver. Eğer cevap bir engel görene kadar ileri veya geri gitmeyi içeriyorsa veya saniye belirtmemisse, komutunuz sadece [sonsuz saniye ileri/geri gidiyorum] olmalıdır öbür türlü x saniye geçiyorsa [x saniye ileri/geri gidiyorum] demelisin. Hiçbir anlamlı komut içeren metin gelmediyse, örneğin 'yumurta 10 gramdır', [Anlamadım] cevabını ver. Ozet gecmek gerekirse senin umursaman gereken komutlar sunlardir : saga/sola/geri dön, x saniye ileri/geri git, engel görene kadar ileri/geri git, ileri/geri git. Ayrıca belirli bir saniye durmanı veya beklemeni söylediğimizde [x saniye dur] şeklinde komut çıkar."
    
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": prompt}
            ],
            temperature=0.1
            )
    
    return response["choices"][0]["message"]["content"]

# reply = ask_chatgpt(user_input)

    
