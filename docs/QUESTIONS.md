# Câu hỏi nghiên cứu — đề xuất và bằng chứng

> **Trạng thái: ĐỀ XUẤT, chưa chốt.** Nhóm thảo luận, kiểm chứng lại trong notebook 01 (Phase 2), sửa lời theo ý mình,
> rồi mới chốt vào [`DECISIONS.md`](DECISIONS.md), bảng Questions trong [`README.md`](../README.md) và ma trận D1–D6
> trong [`PROJECT_PLAN.md`](PROJECT_PLAN.md).
>
> **Nguồn gốc:** các câu hỏi được gợi ý khi brainstorm với Claude Code (ngày 2026-11-01) và đã ghi trong
> [`LLM_USAGE.md`](../LLM_USAGE.md). Đề chỉ cho dùng AI như gia sư (mục 6): phần phân tích, kết luận và câu trả lời phải
> do nhóm tự làm, và mỗi người phải giải thích được vì sao chọn câu của mình.
>
> **Về số liệu trong file này:** đo trên dataset phiên bản 1 ngày 2026-11-01, chỉ để chứng minh **dữ liệu đủ để trả lời**
> và chỉ ra **rủi ro phải xử lý**. Đây **không phải** kết quả phân tích; nhóm phải tự đo lại trong notebook.

## 1. Tổng quan

### 1.1 Số câu và cách chia

Nhóm 2 người → **đúng 4 câu**: **3 câu non-ML + 1 câu ML** (đề, mục 3.3).

- Không làm nhiều hơn 4: đề yêu cầu đúng 2 × n câu, làm thêm không cộng điểm, và 15 phút thuyết trình chỉ đủ khoảng
  3,5 phút cho mỗi câu. Điểm cao đến từ **độ sâu** của từng câu.
- Chỉ 1 câu ML: câu ML tốn công nhất (6 yêu cầu bắt buộc); 3 câu non-ML giúp phủ đủ cả 6 tiêu chí D.
- 4 câu phủ 4 mảng khác nhau của dataset: **giá theo thời gian**, **giá giữa các nền tảng**, **hành vi người chơi**, **review**.

| Câu | Loại | Chủ đề | Notebook | Người sở hữu |
| --- | --- | --- | --- | --- |
| Q1 | non-ML | Đợt sale của Steam: giảm sâu tới đâu, ở đâu, giá có về lại không | `02_analysis_q1.ipynb` | TODO |
| Q2 | non-ML | Cùng một game: console đắt hơn PC bao nhiêu | `02_analysis_q2.ipynb` | TODO |
| Q3 | non-ML | Người chơi bỏ game nhanh tới mức nào sau thành tựu đầu tiên | `02_analysis_q3.ipynb` | TODO |
| Q4 | ML | Dự đoán review Steam có được bình chọn "helpful" không | `03_ml_question.ipynb` | TODO |
| Q4' | ML (dự phòng) | Dự đoán người chơi PlayStation có đạt Platinum không | `03_ml_question.ipynb` | — |

### 1.2 Ma trận tiêu chí độ sâu (dự kiến)

Đề: mỗi câu non-ML dùng ≥ 2 tiêu chí, cả 3 câu gộp lại ≥ 4/6.

| | D1 Ghép dữ liệu | D2 Reshape & thời gian | D3 Biến phái sinh | D4 Kiểm soát nhiễu | D5 Độ bất định | D6 Độ vững |
| --- | --- | --- | --- | --- | --- | --- |
| Q1 | ✅ prices ↔ games | ✅ trước / trong / sau sale | ✅ % giảm giá | ✅ tuổi game, mức giá gốc | ✅ bootstrap CI | ✅ hai đợt sale, hai cách tính giá nền |
| Q2 | ✅ 3 nền tảng | | ✅ tỉ lệ giá console/PC | ✅ năm phát hành, thể loại, mức giá | ✅ kiểm định theo cặp | ✅ hai cách khớp tên, hai ngày giá |
| Q3 | ✅ history ↔ achievements ↔ games | ✅ cohort, đường giữ chân theo ngày | ✅ "còn hoạt động sau N ngày" | ✅ số thành tựu của game, thể loại | ✅ CI cho tỉ lệ giữ chân | ✅ có/không loại dữ liệu nghi hack |
| **Phủ** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

### 1.3 Gợi ý phân công

| Phương án | Thành viên A | Thành viên B | Ghi chú |
| --- | --- | --- | --- |
| Cân bằng khối lượng | Q1 + Q4 | Q2 + Q3 | A dùng dữ liệu Steam; B dùng dữ liệu 3 nền tảng |
| Theo chủ đề | Q1 + Q2 ("Giá") | Q3 + Q4 ("Người chơi") | dễ kể chuyện khi thuyết trình, nhưng phần B nặng hơn |

## 2. Dữ liệu nói gì (bằng chứng chung)

| Bảng | Steam | PlayStation | Xbox | Điểm quan trọng |
| --- | --- | --- | --- | --- |
| `games` | 98.248 | 23.151 | 10.489 | PS có 11.974 dòng trùng tên (cùng game, nhiều bản PS4/PS5/Vita); Steam có 3 game tên rỗng |
| `achievements` | 1.939.027 | 846.563 | 351.111 | PS: 219.605 thành tựu thuộc game **không có** trong `games`; bảng PS có ô nhiều dòng (engine `pyarrow` đọc lỗi) |
| `history` | 10.693.879 | 19.510.083 | 15.275.900 | chỉ khoảng **5.000 người chơi** mỗi nền tảng; 2008-09 → 12/2024 |
| `players` | 424.683 | 356.600 | 274.450 | phần lớn **không** có lịch sử; Steam thiếu `country` 42%, Xbox không có `country` |
| `prices` | 4.414.273 (45 ngày) | 62.816 (3 ngày) | 22.638 (2 ngày) | chỉ Steam có chuỗi thời gian; ngày chung của cả 3: 22–24/02/2025 |
| `purchased_games` | 102.548 | 46.582 | 46.466 | thư viện game của người chơi (không dùng trong 4 câu) |
| `reviews` | 1.204.534 | — | — | 10/2010 → 01/2025, phần lớn từ 2017; `helpful` lệch mạnh (trung vị 0) |
| `friends`, `private_steamids` | 424.683 / 227.963 | — | — | không dùng: mạng bạn bè chỉ có ở Steam, không phục vụ câu hỏi nào có ích cho cả 3 nền tảng |

**Thiên lệch chọn mẫu:** người chơi trong `history` lấy từ bảng xếp hạng Exophase, phần lớn là người "săn thành tựu".
Mọi kết luận về hành vi chỉ đúng cho nhóm này, phải nêu trong phần hạn chế.

---

## 3. Q1 — Đợt sale của Steam (non-ML)

**Câu hỏi (nháp):** Trong các đợt sale lớn của Steam từ 11/2024 đến 02/2025, game được giảm giá sâu tới mức nào? Thể loại và
mức giá nào được giảm mạnh nhất khi đã tính đến tuổi của game? Sau đợt sale, giá có trở về đúng mức cũ không?

> *English draft:* During Steam's major sales between Nov 2024 and Feb 2025, how deep were the discounts, which genres and
> price tiers were discounted most once game age is accounted for, and did prices return to their pre-sale level afterwards?

**Ai quan tâm, quyết định gì:**
- Người mua: có nên chờ sale không, chờ được bao nhiêu.
- Nhà phát triển indie: nên giảm bao nhiêu % để không bị lép vế so với game cùng thể loại, cùng tuổi.

**Bằng chứng từ dataset:**
- `steam/prices`: 45 ngày, cứ 2 ngày một lần, từ 28/11/2024 đến 24/02/2025; mỗi ngày 97.659–98.465 game; không có dòng
  trùng `(gameid, ngày)`. 77.495 game có giá USD dương ở **đủ 45 ngày**.
- Tỉ lệ game có giá thấp hơn giá cao nhất của chính nó trong giai đoạn (dấu hiệu đang giảm giá):

  | Giai đoạn | Tỉ lệ |
  | --- | --- |
  | 28/11 → 04/12/2024 | 59–60% |
  | 06/12 → 18/12/2024 | 7–13% |
  | **20/12/2024 → 01/01/2025** | **61–62%** |
  | 03/01 → 24/02/2025 | 3–14% |

  → Dữ liệu tự cho thấy **hai đợt sale lớn** (cuối tháng 11 và cuối tháng 12), không cần dựa vào lịch Steam.
- 20.049 game **không có giá USD ở bất kỳ ngày nào** (game miễn phí hoặc không bán) → loại, báo số dòng.
- 217 `gameid` có giá nhưng không có trong `games` → báo khi merge (D1).
- `genres` là danh sách dạng chuỗi (`"['Action', 'Indie']"`), 33 nhãn; thiếu 5,6% → cần tách nhãn (`explode`), một game
  thuộc nhiều thể loại.

**Quy trình phân tích:**
1. **Làm sạch:** loại game không có giá USD; chỉ giữ game có giá ở đủ 45 ngày (hoặc nêu rõ quy tắc khác). In số dòng.
2. **Ghép** `prices` ↔ `games` lấy thể loại và ngày phát hành; báo số `gameid` không khớp (D1).
3. **Xác định đợt sale từ dữ liệu:** vẽ tỉ lệ game đang giảm theo ngày, chốt khoảng ngày của mỗi đợt (D2).
4. **Giá nền mỗi game:** trung vị giá ở các ngày ngoài sale. **% giảm** = 1 − giá / giá nền (D3).
5. **Gán giai đoạn** trước / trong / sau từng đợt sale; so sánh % giảm và tỉ lệ game được giảm (D2).
6. **Kiểm soát nhiễu:** so sánh thể loại **trong từng nhóm** tuổi game (năm từ ngày phát hành) và mức giá gốc (D4).
7. **Độ bất định:** bootstrap khoảng tin cậy 95% cho % giảm trung vị của từng thể loại; kiểm định khác biệt kèm effect size (D5).
8. **"Giá có về lại không":** tỉ lệ game sau sale có giá bằng, cao hơn hay thấp hơn giá nền. Có thể kiểm tra thêm game nào
   **tăng giá ngay trước sale** (giảm giá "ảo").
9. **Độ vững:** lặp lại kết luận cho **đợt sale thứ hai**; đổi định nghĩa giá nền (trung vị ↔ giá cao nhất) (D6).

**Biểu đồ gợi ý (≥ 2):** đường tỉ lệ game giảm giá theo ngày, tô màu các đợt sale · biểu đồ khoảng tin cậy % giảm theo thể loại,
tách theo tuổi game · heatmap thể loại × mức giá gốc.

**Rủi ro và cách xử lý:**
- Dữ liệu bắt đầu ngày 28/11, **giữa** đợt sale đầu → đợt đầu không có "trước sale"; đợt thứ hai đủ cả trước/trong/sau.
- Giá USD là giá cửa hàng Mỹ, không đại diện cho mọi khu vực.

**Khác với phân tích đã có:** tác giả chỉ dùng giá trung bình để tính ARPU/LTV, không phân tích diễn biến giá theo thời gian.

---

## 4. Q2 — Console có đắt hơn PC không? (non-ML)

**Câu hỏi (nháp):** Với cùng một game bán trên Steam, PlayStation và Xbox, bản console đắt hơn hay rẻ hơn bản PC bao nhiêu?
Chênh lệch đó có thay đổi theo tuổi game, thể loại và mức giá không?

> *English draft:* For the same game sold on Steam, PlayStation and Xbox, how much more (or less) does the console version
> cost than the PC version, and does the gap depend on game age, genre and price tier?

**Ai quan tâm, quyết định gì:**
- Người chơi chọn mua game trên nền tảng nào.
- Nhà phát hành định giá khi đưa game lên nhiều nền tảng.

**Bằng chứng từ dataset:**
- Ngày **22/02/2025** là ngày đầu tiên cả 3 nền tảng đều có giá. Hôm đó Steam **không** trong đợt sale (8,9% game giảm,
  bằng mức bình thường) → so sánh công bằng.
- Số game có giá USD ngày 22/02/2025: Steam 77.872 · PlayStation 20.193 · Xbox 7.920.
- Số game khớp tên giữa các nền tảng (có giá ngày đó):

  | Cách khớp | Steam & PS | Steam & Xbox | Cả 3 |
  | --- | --- | --- | --- |
  | Tên giữ nguyên (chữ thường) | 5.133 | 5.020 | 3.454 |
  | Tên chuẩn hoá (bỏ ™ ® ©, dấu câu) | 5.591 | 5.425 | 3.787 |

- PlayStation có **11.974 dòng trùng tên** (ví dụ `#KILLALLZOMBIES` có bản PS3, PS4, PS Vita) → phải gộp về một giá
  mỗi tên game theo quy tắc rõ ràng. Steam có 838, Xbox có 944 tên trùng.
- 2,7–5,2% tên game có chữ "Edition", "Deluxe", "Bundle"… → dễ khớp nhầm phiên bản khác nhau.

**Quy trình phân tích:**
1. **Chuẩn hoá tên** và **gộp tên trùng** trong từng nền tảng (ví dụ: lấy giá thấp nhất, hoặc ưu tiên bản PS5); in số dòng.
2. **Ghép 3 nền tảng** theo tên chuẩn hoá; báo số game khớp, không khớp ở từng cặp (D1).
3. **Biến phái sinh:** `log(giá console / giá Steam)` cho PS và Xbox (D3); lấy log để chênh lệch đối xứng.
4. **So sánh theo cặp:** Wilcoxon signed-rank hoặc bootstrap khoảng tin cậy cho trung vị tỉ lệ; báo effect size (D5).
5. **Kiểm soát nhiễu:** so sánh chênh lệch trong từng nhóm năm phát hành, thể loại, mức giá Steam (D4).
6. **Độ vững:** khớp tên chính xác ↔ chuẩn hoá; có/không loại tên chứa "Edition/Bundle"; dùng giá ngày 24/02 thay cho 22/02 (D6).

**Biểu đồ gợi ý (≥ 2):** scatter giá Steam vs giá console (trục log, có đường y = x) · phân phối log-tỉ lệ cho PS và Xbox ·
log-tỉ lệ theo năm phát hành.

**Rủi ro và cách xử lý:**
- Khớp theo tên có thể sai (cùng tên khác game, hoặc khác phiên bản) → kiểm tra bằng tay một mẫu ngẫu nhiên và báo tỉ lệ sai.
- Không biết game console có đang giảm giá ngày đó không (chỉ có 2–3 ngày giá) → nêu trong hạn chế; so sánh 22/02 và 24/02.
- Năm phát hành và thể loại lấy từ bảng Steam để thống nhất giữa 3 nền tảng.

**Khác với phân tích đã có:** tác giả không so sánh giá giữa các nền tảng.

---

## 5. Q3 — Người chơi bỏ game nhanh tới mức nào? (non-ML)

**Câu hỏi (nháp):** Sau thành tựu đầu tiên trong một game, bao nhiêu % người chơi vẫn còn mở thành tựu mới sau 7, 30 và 90 ngày?
Mức giữ chân này khác nhau thế nào giữa Steam, PlayStation, Xbox và giữa các thể loại, khi đã tính đến số thành tựu của game?

> *English draft:* After a player's first achievement in a game, what share of players still unlock new achievements 7, 30
> and 90 days later, and how does this retention differ across Steam, PlayStation and Xbox and across genres once the number
> of achievements in the game is accounted for?

**Ai quan tâm, quyết định gì:**
- Nhà phát triển: nội dung và thành tựu nên rải tới mốc nào để giữ người chơi.
- Nền tảng: thời điểm nào nên gửi thông báo, gợi ý để kéo người chơi quay lại.

**Bằng chứng từ dataset:**
- `history` ghép với `achievements` khớp **100%** ở cả 3 nền tảng; không có dòng trùng `(người chơi, thành tựu)`.
- Số cặp (người chơi, game): Steam 276.036 · PS 995.079 · Xbox 1.010.783; mỗi năm 2019–2024 có 22–95 nghìn cặp mới
  mỗi nền tảng → đủ lớn cho phân tích cohort.
- Game đã chơi **không có** trong bảng `games` (mất thể loại): Steam 58 · Xbox 742 · **PS 5.969** (≈ 26% game đã chơi) → phải báo (D1)
  và phân tích thể loại trên phần khớp được.
- **Dấu hiệu hack/đồng bộ hàng loạt:** tỉ lệ lượt mở thành tựu trùng đúng một giây với ≥ 5 thành tựu khác của cùng người chơi:
  **Steam 55,3%** · PS 1,5% · Xbox 1,3% → bắt buộc kiểm tra độ vững.
- Dữ liệu kết thúc 15/12 (Steam), 29/12 (PS), 24/12/2024 (Xbox); 6–13 nghìn cặp bắt đầu trong 90 ngày cuối → chưa đủ thời gian
  quan sát, phải loại khi tính mốc 90 ngày.
- Ngày sớm nhất của cả 3 nền tảng đều là 12–13/09/2008 (PS 116 dòng, Xbox 982 dòng ngày đó) → nghi là ngày mặc định khi thiếu
  ngày thật; kiểm tra trong notebook 01.

**Quy trình phân tích:**
1. **Ghép** `history` → `achievements` (lấy `gameid`) → `games` (thể loại); báo số dòng và key không khớp (D1).
2. **Gom về mức (người chơi, game):** ngày mở đầu tiên, ngày mở cuối cùng, số thành tựu đã mở. Lưu bảng này vào
   `data/processed/` vì `history` rất nặng.
3. **Biến phái sinh:** `active_after_N` = có mở thành tựu nào sau ngày đầu tiên + N ngày (N = 7, 30, 90) (D3).
4. **Xử lý censoring:** chỉ giữ cặp bắt đầu sớm hơn ngày cuối của dữ liệu ít nhất N ngày; in số dòng mỗi lần lọc.
5. **Đường giữ chân và cohort:** tỉ lệ còn hoạt động theo số ngày; bảng cohort theo quý bắt đầu chơi (D2).
6. **Kiểm soát nhiễu:** so sánh nền tảng và thể loại **trong từng nhóm** số thành tựu của game (game ít và nhiều thành tựu khác nhau tự nhiên) (D4).
7. **Độ bất định:** khoảng tin cậy cho tỉ lệ giữ chân; bootstrap theo **người chơi**, vì một người có nhiều cặp (D5).
8. **Độ vững:** chạy lại sau khi loại các cặp có dấu hiệu mở hàng loạt cùng một giây; đổi mốc N; giới hạn 2019–2024 (D6).

**Biểu đồ gợi ý (≥ 2):** đường giữ chân của 3 nền tảng (trục x: ngày kể từ thành tựu đầu) · heatmap cohort × mốc ngày ·
tỉ lệ còn hoạt động sau 30 ngày theo thể loại, tách theo nhóm số thành tựu.

**Rủi ro và cách xử lý:**
- "Không mở thành tựu mới" **không chắc** là "bỏ game" (có game rất ít thành tựu, hoặc người chơi đã mở hết) → nêu rõ định nghĩa;
  có thể loại cặp đã mở hết thành tựu của game.
- Mẫu là người săn thành tựu → kết luận không áp dụng cho người chơi phổ thông.

**Khác với phân tích đã có:** tác giả đo **tỉ lệ hoàn thành** (% thành tựu đạt được) và MAU/WAU. Câu này đo **tốc độ rời bỏ theo
thời gian** sau khi bắt đầu một game. Vẫn phải khai báo trong README vì cùng chủ đề hành vi người chơi.

---

## 6. Q4 — Review nào sẽ được bình chọn "helpful"? (ML)

**Câu hỏi (nháp):** Ngay khi một review Steam vừa được đăng, có dự đoán được review đó cuối cùng nhận ít nhất một lượt
"helpful" không? Những đặc điểm nào của review, người viết và game quyết định điều đó?

> *English draft:* At the moment a Steam review is posted, can we predict whether it will receive at least one "helpful"
> vote, and which characteristics of the review, its author and the game drive that prediction?

**Người dùng của dự đoán:** Steam (hoặc một trang tổng hợp review) cần xếp hạng review **mới** khi chưa có lượt bình chọn nào,
để người mua đọc được review hữu ích sớm hơn.

**Bằng chứng từ dataset:**
- 1.204.534 review, không trùng `reviewid`, không trùng `(người chơi, game)`; 2.097 review thiếu nội dung.
- **Target** `helpful > 0`: **34%** dương → mất cân bằng vừa phải; accuracy dễ gây hiểu nhầm (đoán toàn "không" đã đúng 66%).
- **Hiệu ứng thời gian phơi bày:** tỉ lệ được vote theo năm đăng: 2017 41,6% · 2018 41,1% · 2019–2024 29–34% · 2025 24,5%
  (mới đăng, chưa kịp được vote) → review càng cũ càng có nhiều thời gian nhận vote.
- Độ dài: trung vị 9 từ; **32,7%** review có ≤ 3 từ; khoảng 41,5% review không phải văn bản ASCII (nhiều ngôn ngữ).
- Ghép: 100% tác giả review có trong `players` (thiếu ngày tạo tài khoản 10,3%); 161 game được review không có trong `games`.

**Đủ 6 yêu cầu ML của đề:**

| Yêu cầu | Kế hoạch |
| --- | --- |
| 1. Bài toán, người dùng, chống leakage | Phân loại nhị phân `helpful > 0` tại thời điểm đăng. **Loại:** `helpful` (chính là target), `funny`, `awards` (bình chọn đến **sau** khi đăng), `purchased_games`, `friends` (ảnh chụp năm 2025, không phải lúc đăng), giá game (chỉ có giá 2024–25). |
| 2. Chia dữ liệu | **Theo thời gian** theo `posted`: ví dụ train 2018–2022, test 2023. Bỏ 2024–2025 vì chưa đủ thời gian nhận vote (giải thích bằng bảng ở trên). |
| 3. ≥ 2 mô hình + baseline, `Pipeline` | Baseline: đoán lớp đa số / tỉ lệ dương. Mô hình: Logistic Regression, HistGradientBoosting. Mọi bước (impute, scale, one-hot, TF-IDF nếu dùng) nằm trong `Pipeline` + `ColumnTransformer`. |
| 4. Tune bằng CV trên train, test một lần, metric có lý do | `TimeSeriesSplit` trên tập train; metric chính **PR-AUC (average precision)**, phụ là F1 tại ngưỡng chọn trên train. |
| 5. Phân tích lỗi | Theo độ dài review, ngôn ngữ (ASCII/không), độ phổ biến của game, tuổi tài khoản; xem ví dụ dự đoán sai. |
| 6. Diễn giải, trả lời câu hỏi | Permutation importance trên tập test; trả lời: đặc điểm nào khiến review được bình chọn. |

**Feature gợi ý (đều có tại thời điểm đăng):** số từ, số ký tự, có xuống dòng/liên kết, tỉ lệ chữ hoa, ASCII hay không ·
tuổi tài khoản lúc đăng (`posted − created`) · số review người đó đã viết **trước** đó · số ngày từ khi game phát hành ·
số review game đó đã có **trước** thời điểm đăng · thể loại game.

**Rủi ro và cách xử lý:**
- Hiệu ứng thời gian phơi bày (ở trên) → chia theo thời gian và giới hạn năm; nêu trong hạn chế.
- Các feature "trước thời điểm đăng" phải tính chỉ từ dữ liệu quá khứ, nếu không sẽ leakage.
- Một game có nhiều review ở cả train và test → báo trong phân tích lỗi (game phổ biến có thể làm mô hình "học thuộc").

**Khác với phân tích đã có:** tác giả không phân tích bảng `reviews`.

---

## 7. Q4' — Dự phòng cho câu ML: đạt Platinum trên PlayStation

**Câu hỏi (nháp):** Dựa vào 7 ngày đầu chơi một game PlayStation, có dự đoán được người chơi cuối cùng có đạt trophy Platinum không?

**Bằng chứng:** 25.589 game có Platinum; 863.919 cặp (người chơi, game) trên các game đó; **32,2%** đạt Platinum; mỗi năm
2019–2024 có 60–89 nghìn cặp mới. Dữ liệu PS ít dấu hiệu mở hàng loạt (1,5%), hợp với feature "tuần đầu".

**Hướng làm:** feature từ 7 ngày đầu (số trophy, tỉ lệ Gold/Silver, số ngày có hoạt động), đặc điểm game (tổng số trophy,
PS4/PS5), lịch sử người chơi **trước** game đó (tỉ lệ Platinum ở các game trước). Chia theo thời gian bắt đầu chơi hoặc
`GroupKFold` theo người chơi. Loại mọi thông tin sau ngày thứ 7.

**Vì sao chỉ là dự phòng:** gần với chủ đề **tỉ lệ hoàn thành** mà tác giả đã phân tích → phải khai báo kỹ; và 26% game PS đã
chơi không có trong `games` nên thiếu thể loại.

---

## 8. Việc tiếp theo

- [ ] Hai thành viên đọc file này, chọn giữ / sửa / thay từng câu (ghi lý do vào [`DECISIONS.md`](DECISIONS.md)).
- [ ] Trong Phase 2, đo lại các số liệu ở trên trong notebook 01 bằng code của nhóm.
- [ ] Xem tab *Code* của dataset trên Kaggle, đảm bảo không trùng câu hỏi; ghi vào README mục *Related public work*.
- [ ] Chốt người sở hữu từng câu (mục 1.3).
- [ ] Viết lại câu hỏi bằng lời của nhóm, cập nhật README (tiếng Anh), notebook 02/03 (mục 1–3) và ma trận trong `PROJECT_PLAN.md`.
