# Monty Hall Problemi

Monty Hall problemi, Amerikan TV yarışma programı Let's Make a Deal'a dayanan bir olasılık bulmacasıdır. Problem adını, yarışmanın sunucusu olan Monty Hall'dan alır. 

Problemi temel olarak şu soru oluşturmaktadır: "Bir yarışma programında olduğunuzu ve üç kapıdan birini seçme hakkınız olduğunu varsayalım. Kapılardan birinin ardında bir araba, diğerlerinin ardında ise birer keçi var. Kapılardan birini seçiyorsunuz ve kapıların ardında ne olduğunu bilen sunucu, diğer kapılardan ardında keçi olan kapıyı açıyor. Daha sonra size soruyor: "Kapınızı diğer kapı ile değiştirmek ister misiniz?" Seçiminizi değiştirmek sizin yararınıza mıdır?"

Bu soruya cevabınız 'Evet' ise olasılıksal olarak arabayı kazanma ihtimaliniz 'Hayır' cevabını verenlere göre daha yüksektir. Yani araba kazanma olasılığınız kabaca 1/3'ten 2/3'e yükselerek iki katına çıkar. Araba kazanma olasılığınızın iki durum için de 1/3 olduğunu ve olasılığın değişmeyeceğini düşünüyorsanız şöyle açıklayayım:

Yarışmanın konseptinin şu şekilde olduğunu düşünelim. Sunucu önce sizden bir kapı seçmenizi istiyor. Ardından sizin seçtiğiniz kapıya karşılık seçmediğiniz diğer 2 kapıyı size vermeyi teklif ediyor. Böyle bir durumda hiç düşünmeden kararınızı değiştirirsiniz. Araba olan kapıyı bulma ihtimaliniz ikiye katlanır çünkü artık 1 kapı yerine 2 kapıya sahipsiniz. Sunucu arkasında keçi olan kapıyı açmasa bile bu, o kapıların birinin ardında keçi olduğu gerçeğini değiştirmez. Diğer bir deyişle aslında arkasında keçi olan kapıyı açıp açmamak olasılıksal olarak herhangi bir etki yapmayacaktır.

Daha kolay anlamak adına yarışmayı daha farklı bir konseptte düşünelim. Bu sefer önünüzde seçmek için 100 adet kapı var ve sadece 1 tanesinin arkasında bir araba, diğer hepsinin arkasında birer keçi var. Sunucu bir kapı seçmenizi istediğinizde 37 numaralı kapıyı seçtiğinizi varsayalım. Daha sonra sunucu da 61 numaralı kapı hariç diğer bütün arkasında keçi olan kapıları açıp size kapınızı değiştirmek isteyip istemediğinizi sorsun. Bu durumda cevabınız ne olurdu? İlk başta %1 olan araba kazanma ihtimaliniz kapınızı değiştirirseniz %99'a çıkacaktır. Böyle bir durumda kim olursa olsun 61 numaralı kapıyı seçecektir. Tabi eğer amacı araba değil de keçi kazanmaksa durumlar değişir :)

Repository içerisindeki 'monty_hall_problem.py' adlı dosyayı çalıştırarak yarışmanın oyununu oynayabilir ya da 'monty_hall_automated.py' isimli dosyayı çalıştırarak oyunu bilgisayarın 1000 kere oynamasını ve olasılık sonuçlarını size göstermesini sağlayabilirsiniz.

Kodlarda veya içerikte bir yanlışlık, hata görmeniz durumunda geri bildirim sağlamanızdan mutluluk duyarım. İyi eğlenceler :)
