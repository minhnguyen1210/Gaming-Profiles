# Câu hỏi nghiên cứu — đề xuất và bằng chứng

> **Trạng thái: ĐỀ XUẤT, chưa chốt.** Nhóm làm xong notebook 01 (Phase 2) trước, kiểm chứng lại các số liệu ở đây, rồi mới
> chọn 4 câu và người sở hữu ([`DECISIONS.md`](DECISIONS.md) #6). Khi chốt thì ghi vào `DECISIONS.md`, bảng Questions
> trong [`README.md`](../README.md) và ma trận D1–D6 trong [`PROJECT_PLAN.md`](PROJECT_PLAN.md).
>
> **Nguồn gốc:** bộ câu đầu tiên được gợi ý khi brainstorm với Claude Code (2026-11-01). Ngày 2026-11-20, Claude Code
> rà soát lại bộ câu đó trên dữ liệu thật, thử thêm 6 hướng mới, rồi đề xuất bộ 4 câu dưới đây (thay câu Q2 cũ, sửa
> Q1, Q3, Q4). Cả hai lần phải ghi trong [`LLM_USAGE.md`](../LLM_USAGE.md). Đề chỉ cho dùng AI như gia sư (mục 6): phần
> phân tích, kết luận và câu trả lời phải do nhóm tự làm, và mỗi người phải giải thích được vì sao chọn câu của mình.
>
> **Về số liệu trong file này:** đo trên dataset phiên bản 1 (ngày 2026-11-01 và 2026-11-20), chỉ để chứng minh **dữ liệu
> đủ để trả lời** và chỉ ra **rủi ro phải xử lý**. Đây **không phải** kết quả phân tích; nhóm phải tự đo lại trong notebook.

## 1. Tổng quan

### 1.1 Số câu và cách chia

Nhóm 2 người → **đúng 4 câu**: **3 câu non-ML + 1 câu ML** (đề, mục 3.3).

- Không làm nhiều hơn 4: đề yêu cầu đúng 2 × n câu, làm thêm không cộng điểm, và 15 phút thuyết trình chỉ đủ khoảng
  3,5 phút cho mỗi câu. Điểm cao đến từ **độ sâu** của từng câu.
- Chỉ 1 câu ML: câu ML tốn công nhất (6 yêu cầu bắt buộc); 3 câu non-ML giúp phủ đủ cả 6 tiêu chí D.
- 4 câu phủ 4 mảng khác nhau của dataset: **giá theo thời gian**, **thiết kế thành tựu**, **hành vi người chơi**, **review**.

| Câu | Loại | Chủ đề | Dữ liệu chính | Notebook | Người sở hữu |
| --- | --- | --- | --- | --- | --- |
| Q1 | non-ML | Đợt sale Steam: giảm sâu tới đâu, sau sale giá có tăng lên không | Steam `prices`, `games` | `02_analysis_q1.ipynb` | TODO |
| Q2 | non-ML | Hạng trophy PlayStation có phản ánh độ khó thật không | PS `history`, `achievements` | `02_analysis_q2.ipynb` | TODO |
| Q3 | non-ML | Sau thành tựu đầu tiên, người chơi có quay lại game không | `history`, `achievements` cả 3 nền tảng | `02_analysis_q3.ipynb` | TODO |
| Q4 | ML | Dự đoán review Steam có được ≥ 2 vote "helpful" không | Steam `reviews`, `players`, `games` | `03_ml_question.ipynb` | TODO |

### 1.2 Ma trận tiêu chí độ sâu (dự kiến)

Đề: mỗi câu non-ML dùng ≥ 2 tiêu chí, cả 3 câu gộp lại ≥ 4/6.

| | D1 Ghép dữ liệu | D2 Reshape & thời gian | D3 Biến phái sinh | D4 Kiểm soát nhiễu | D5 Độ bất định | D6 Độ vững |
| --- | --- | --- | --- | --- | --- | --- |
| Q1 | ✅ prices ↔ games | ✅ trước / trong / sau sale | ✅ giá nền, % giảm | ✅ tuổi game, mức giá gốc | ✅ bootstrap CI | ✅ hai cách tính giá nền, ngưỡng "đang sale" |
| Q2 | ✅ history ↔ achievements ↔ games | | ✅ tỉ lệ mở thực tế | ✅ so trong từng game (nghịch lý Simpson) | ✅ bootstrap theo game | ✅ đổi ngưỡng số người tối thiểu mỗi game |
| Q3 | ✅ history ↔ achievements | ✅ cohort theo quý (tuỳ chọn) | ✅ "quay lại sau N ngày" | ✅ số thành tựu của game | ✅ bootstrap theo người chơi | ✅ đổi mốc N; loại cặp mở hàng loạt |
| **Phủ** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

### 1.3 Độ khó và gợi ý phân công

Ước lượng công sức rất thô, chỉ để so sánh tương đối giữa các câu.

| Câu | Độ khó | Công sức ước lượng | Phần khó nhất |
| --- | --- | --- | --- |
| Q1 | dễ nhất | 15–20 giờ | định nghĩa đợt sale và giá nền |
| Q2 | vừa | 20–25 giờ | giải thích nghịch lý Simpson khi thuyết trình và Q&A |
| Q3 | khó | 25–30 giờ | dữ liệu nặng (khoảng 45 triệu dòng), định nghĩa chỉ số, censoring |
| Q4 | khó nhất | 30–35 giờ | đủ 6 yêu cầu ML, chống leakage, scikit-learn chưa học trên lớp |

| Phương án | Thành viên A | Thành viên B | Ghi chú |
| --- | --- | --- | --- |
| **Cân bằng khối lượng (khuyên dùng)** | Q1 + Q4 | Q2 + Q3 | mỗi người một câu vừa + một câu nặng; Q2 và Q3 cùng dùng `history` |
| Theo nhóm bảng khám phá | Q1 + Q2 | Q3 + Q4 | B giữ cả hai câu nặng nhất → **lệch** |

Notebook 01 chia theo nhóm bảng như PR #1 (A phía game, B phía người chơi; [`DECISIONS.md`](DECISIONS.md) #6):
khám phá xong toàn bộ dữ liệu rồi mới chọn câu hỏi.

### 1.4 Phạm vi kỹ thuật

Mọi câu non-ML làm được hoàn toàn bằng kiến thức đã học trên lớp: Pandas (`merge`, `groupby`, `pivot`, `explode`,
datetime), Regex (tách nhãn thể loại, đếm từ), NumPy (bootstrap bằng `np.random.default_rng(RANDOM_STATE)`), Matplotlib.

- **Không dùng** kiểm định của scipy, hồi quy của statsmodels, hay TF-IDF: chưa học, và không cần để đạt tiêu chí.
  Độ bất định (D5) tính bằng bootstrap với NumPy.
- **scikit-learn chưa học** nhưng đề **bắt buộc** cho câu ML (`Pipeline`, cross-validation). Người giữ Q4 cần học sớm;
  hỏi lại giảng viên xem môn có dạy ở các buổi sau không.
- Ba khái niệm cần hiểu để trả lời Q&A: **censoring** (Q3), **nghịch lý Simpson** (Q2), **data leakage** (Q4).

## 2. Dữ liệu nói gì (bằng chứng chung)

| Bảng | Steam | PlayStation | Xbox | Điểm quan trọng |
| --- | --- | --- | --- | --- |
| `games` | 98.248 | 23.151 | 10.489 | không thiếu `release_date`; Steam có 5.294 tên chứa "Playtest"; PS có nhiều dòng cùng tên (bản PS3/PS4/PS5/Vita) |
| `achievements` | 1.939.027 | 846.563 | 351.111 | PS có cột `rarity` (Bronze/Silver/Gold/Platinum), Xbox có cột `points`; bảng PS có ô nhiều dòng (engine `pyarrow` đọc lỗi) |
| `history` | 10.693.879 | 19.510.083 | 15.275.900 | chỉ 4.838 / 5.000 / 4.984 người chơi; 2008-09 → 12/2024 |
| `players` | 424.683 | 356.600 | 274.450 | phần lớn **không** có lịch sử; Steam thiếu `country` 41,9%; Xbox không có `country` |
| `prices` | 4.414.273 (45 ngày) | 62.816 (3 ngày) | 22.638 (2 ngày) | chỉ Steam có chuỗi thời gian |
| `purchased_games` | 102.548 | 46.582 | 46.466 | Steam: 54,2% thư viện là ô rỗng (không công khai) |
| `reviews` | 1.204.534 | — | — | 10/2010 → 01/2025; không có cột "đề xuất / không đề xuất" |
| `friends`, `private_steamids` | 424.683 / 227.963 | — | — | không dùng trong 4 câu |

**Thiên lệch chọn mẫu:** người chơi trong `history` lấy từ bảng xếp hạng Exophase, phần lớn là người "săn thành tựu".
Mọi kết luận về hành vi (Q2, Q3) chỉ đúng cho nhóm này, phải nêu trong phần hạn chế.

---

## 3. Q1 — Đợt sale Steam: giảm sâu tới đâu, sau sale giá có tăng lên không? (non-ML)

**Câu hỏi (nháp):** Trong đợt sale cuối năm 2024 của Steam, game được giảm giá sâu tới mức nào, và mức giảm khác nhau thế nào
theo tuổi game và mức giá gốc? Sau khi sale kết thúc, bao nhiêu game quay về đúng giá cũ, bao nhiêu game **tăng giá**?

> *English draft:* During Steam's 2024 winter sale, how deep were the discounts and how did they vary with game age and
> original price tier? After the sale, what share of games returned to their pre-sale price, and what share became more
> expensive?

**Ai quan tâm, quyết định gì:**
- Người mua: có nên chờ sale không; mua ngay sau sale có bị đắt hơn trước không.
- Nhà phát triển: nên giảm bao nhiêu % so với game cùng tuổi, cùng mức giá.

**Bằng chứng từ dataset:**
- `steam/prices`: 45 ngày, cứ 2 ngày một lần, 28/11/2024 → 24/02/2025; không có dòng trùng `(gameid, ngày)`.
  77.495 game có giá USD dương ở **đủ 45 ngày**; 20.049 game không có giá USD ở ngày nào (miễn phí hoặc không bán).
- Tỉ lệ game có giá thấp hơn giá cao nhất của chính nó trong giai đoạn:

  | Giai đoạn | Tỉ lệ |
  | --- | --- |
  | 28/11 → 04/12/2024 | 60% (đợt sale thứ nhất, **không có** giai đoạn "trước sale") |
  | 06/12 → 18/12/2024 | 7–13% |
  | **20/12/2024 → 01/01/2025** | **61–62%** (đợt sale cuối năm) |
  | 03/01 → 24/02/2025 | 3–14% |

- **Dấu hiệu tăng giá sau sale:** tỉ lệ game có giá **cao hơn** giá trung vị của chính nó là 0,1–2,4% trước 03/01 nhưng
  khoảng **5%** từ 03/01. So giá ngày 18/12 (trước sale) với ngày 24/02: 83,8% giữ nguyên, **7,7% tăng**, 8,4% giảm.
- 24.976 / 77.495 game (32%) không đổi giá lần nào trong 45 ngày → phải nói rõ có tính vào mẫu số hay không.
- 217 `gameid` có giá nhưng không có trong `games` → báo khi merge (D1). Trong các game giữ lại: thiếu `genres` 0,1%,
  không thiếu `release_date`; `genres` là chuỗi dạng danh sách, 33 nhãn → tách bằng regex rồi `explode`.

**Quy trình phân tích:**
1. **Làm sạch:** chỉ giữ game có giá USD dương ở đủ 45 ngày; in số dòng.
2. **Ghép** `prices` ↔ `games` lấy thể loại và ngày phát hành; báo số `gameid` không khớp (D1).
3. **Xác định đợt sale từ dữ liệu:** vẽ tỉ lệ game đang giảm giá theo ngày; chốt ngưỡng (ví dụ > 30% game đang giảm) (D2).
4. **Giá nền** mỗi game: trung vị giá ở các ngày ngoài sale. **% giảm** = 1 − giá / giá nền (D3).
5. **Trước / trong / sau** đợt sale cuối năm: so sánh % giảm và tỉ lệ game được giảm (D2).
6. **Kiểm soát nhiễu:** so sánh trong từng nhóm tuổi game (năm kể từ ngày phát hành) và mức giá gốc (D4).
7. **Độ bất định:** bootstrap khoảng tin cậy 95% bằng NumPy cho % giảm trung vị và cho tỉ lệ game tăng giá (D5).
8. **"Giá có về lại không":** tỉ lệ game sau sale có giá bằng, cao hơn, thấp hơn giá trước sale; xem tay vài ví dụ tăng giá.
9. **Độ vững:** đổi định nghĩa giá nền (trung vị ↔ giá cao nhất ngoài sale); đổi ngưỡng "đang sale" (D6).

**Biểu đồ gợi ý (≥ 2):** đường tỉ lệ game đang giảm giá theo ngày, tô màu đợt sale · % giảm theo tuổi game × mức giá
(heatmap) · cột tỉ lệ game giữ giá / tăng / giảm sau sale, kèm khoảng tin cậy.

**Rủi ro và cách xử lý:**
- Đợt sale thứ nhất không có giai đoạn trước sale → chỉ phân tích sâu đợt cuối năm; không dùng đợt thứ nhất làm D6.
- Câu "thể loại nào giảm sâu nhất" dễ chỉ là một `groupby` → chiều sâu phải nằm ở D4 và ở phần tăng giá sau sale.
- Giá USD là giá cửa hàng Mỹ, không đại diện mọi khu vực.

**Giảm tải nếu cần:** bỏ phân tích theo thể loại, chỉ giữ tuổi game và mức giá; vẫn đủ ≥ 4 tiêu chí.

**Khác với phân tích đã có:** tác giả chỉ dùng giá trung bình để tính ARPU/LTV, không phân tích diễn biến giá theo thời gian.

---

## 4. Q2 — Hạng trophy PlayStation có phản ánh độ khó thật không? (non-ML)

**Câu hỏi (nháp):** Trophy Bronze, Silver, Gold trên PlayStation có thật sự khó dần, đo bằng tỉ lệ người chơi mở được?
Vì sao khi gộp mọi game lại, trophy Gold trông còn **dễ** hơn Bronze?

> *English draft:* Do PlayStation trophy grades (Bronze, Silver, Gold) reflect how hard trophies really are, measured by the
> share of players who unlock them, and why do Gold trophies look easier than Bronze ones when all games are pooled?

**Ai quan tâm, quyết định gì:**
- Nhà phát triển: gán hạng trophy có khớp với độ khó thật không.
- Người săn thành tựu: hạng trophy có dùng được để ước lượng công sức không.

**Bằng chứng từ dataset:**
- `history` PS ghép `achievements` khớp **100%**; chỉ cần gom **một lần** về bảng mức trophy (khoảng 160 nghìn dòng)
  rồi lưu vào `data/processed/`.
- Tỉ lệ mở = số người mở trophy / số người có ít nhất 1 trophy trong game đó. Với các game có ≥ 30 người chơi
  (4.439 game; 101.385 Bronze, 37.769 Silver, 18.679 Gold, 3.638 Platinum), **tỉ lệ mở trung vị**:

  | Bronze | Silver | Gold | Platinum |
  | --- | --- | --- | --- |
  | 45,9% | 37,5% | **50,0%** | 26,3% |

- **Nhưng trong từng game** (3.843 game có cả Bronze và Gold): trung bình chỉ **16,5%** trophy Bronze khó hơn trophy Gold
  trung vị của cùng game → khi so trong cùng game, Gold khó hơn. Đây là dấu hiệu **nghịch lý Simpson**: kết quả gộp bị
  thành phần game làm méo.
- Số ngày trung vị từ trophy đầu tiên tới khi mở: Gold **0** ngày, Bronze 2, Silver 4, Platinum 5 → nhiều trophy Gold
  được mở ngay ngày đầu (game "Platinum dễ"?). Cần kiểm chứng.

**Quy trình phân tích:**
1. **Ghép** `history` → `achievements` (lấy `gameid`, `rarity`) → `games` (năm phát hành, PS4/PS5); báo số dòng và key
   không khớp (D1). 5.969 / 23.025 game đã chơi không có trong `games` → chỉ ảnh hưởng nếu dùng thông tin từ `games`.
2. **Gom** về mức trophy: số người mở; về mức game: số người chơi. Lưu vào `data/processed/`.
3. **Biến phái sinh:** tỉ lệ mở thực tế; số ngày từ trophy đầu tiên của người chơi tới khi mở (D3).
4. **So sánh gộp:** tỉ lệ mở theo hạng trên toàn bộ trophy.
5. **So sánh trong từng game (D4):** với mỗi game, so trung vị tỉ lệ mở của Gold với Bronze; tính % game mà Gold khó hơn
   Bronze. Giải thích vì sao kết quả gộp khác (ví dụ: game có nhiều Gold và rất dễ chiếm tỉ trọng lớn).
6. **Độ bất định:** bootstrap **theo game** bằng NumPy cho % game mà Gold khó hơn Bronze (D5).
7. **Độ vững:** đổi ngưỡng số người tối thiểu mỗi game (30 ↔ 100); tách riêng PS4 và PS5 (D6).

**Biểu đồ gợi ý (≥ 2):** boxplot tỉ lệ mở theo hạng (gộp) đặt cạnh boxplot chênh lệch Gold − Bronze trong từng game ·
scatter mỗi game: tỉ lệ Gold trong game × tỉ lệ mở trung bình, để minh hoạ nghịch lý Simpson.

**Rủi ro và cách xử lý:**
- Mẫu số "người đã bắt đầu game" là lựa chọn chủ quan → nêu rõ định nghĩa.
- Platinum tự mở khi có đủ trophy khác → phân tích riêng hoặc loại khỏi so sánh chính.
- Mẫu là người săn thành tựu → "độ khó" là độ khó với nhóm này.
- Phải hiểu và giải thích bằng lời được nghịch lý Simpson (Q&A chắc chắn hỏi).

**Giảm tải nếu cần:** chỉ làm PlayStation; mở rộng sang điểm `points` của Xbox để làm sau nếu còn thời gian.

**Khác với phân tích đã có:** tác giả đo tỉ lệ hoàn thành game và phát hiện gian lận thành tựu, không đối chiếu hạng trophy
với độ khó thực tế.

---

## 5. Q3 — Sau thành tựu đầu tiên, người chơi có quay lại game không? (non-ML)

**Câu hỏi (nháp):** Sau thành tựu đầu tiên trong một game, bao nhiêu % người chơi **quay lại** mở thêm thành tựu sau 30 ngày?
Tỉ lệ này khác nhau thế nào giữa Steam, PlayStation và Xbox khi so trong cùng nhóm số thành tựu của game?

> *English draft:* After a player's first achievement in a game, what share of players come back and unlock another
> achievement more than 30 days later, and how does this differ across Steam, PlayStation and Xbox once the number of
> achievements in the game is accounted for?

**Ai quan tâm, quyết định gì:**
- Nhà phát triển: nội dung và thành tựu nên rải tới mốc nào để người chơi quay lại.
- Nền tảng: thời điểm nào nên nhắc người chơi quay lại game.

**Định nghĩa (phải ghi rõ trong notebook):** một cặp (người chơi, game) "quay lại sau N ngày" nếu có thành tựu mở **sau**
ngày đầu tiên + N ngày. Đây là "**từng quay lại**" (kể cả quay lại sau nhiều năm), **không** phải "chơi liên tục".

**Bằng chứng từ dataset:**
- `history` ghép `achievements` khớp **100%** ở cả 3 nền tảng.
- Số cặp (người chơi, game): Steam 276.036 · PS 995.079 · Xbox 1.010.783; mỗi năm 2019–2024 có 22–95 nghìn cặp mới mỗi nền tảng.
- Tỉ lệ thô "quay lại sau N ngày":

  | | 7 ngày | 30 ngày | 90 ngày |
  | --- | --- | --- | --- |
  | Steam | 46% | 36% | 31% |
  | PlayStation | 48% | 32% | 24% |
  | Xbox | 46% | 34% | 27% |

- Cặp đã mở **hết** thành tựu của game: Steam 10,7% · PS 26,3% · Xbox 16,1%; cặp chỉ có **1** thành tựu: 9,5–13,5%.
- Mở hàng loạt (≥ 5 thành tựu trong cùng một giây): Steam 55,3% số lượt mở, nhưng tập trung trong chỉ 7,2% số cặp; loại các
  cặp này thì tỉ lệ thay đổi < 1 điểm % → D6 sẽ cho kết luận "vững".
- Mỗi người chơi có rất nhiều cặp (trung vị Steam 29, PS 129, Xbox 121) → các cặp không độc lập, phải bootstrap theo người chơi.
- Dữ liệu kết thúc 15/12 (Steam), 29/12 (PS), 24/12/2024 (Xbox) → cặp bắt đầu sát cuối chưa đủ thời gian quan sát (censoring).

**Quy trình phân tích:**
1. **Ghép** `history` → `achievements` (lấy `gameid`); báo số dòng và key không khớp (D1). Đọc **từng nền tảng một**.
2. **Gom về mức (người chơi, game):** ngày mở đầu tiên, ngày mở cuối cùng, số thành tựu đã mở, tổng số thành tựu của game.
   Lưu vào `data/processed/` vì `history` rất nặng.
3. **Biến phái sinh:** `returned_N` (D3).
4. **Lọc:** chỉ giữ cặp bắt đầu trong 2019–2024; bỏ cặp bắt đầu ít hơn N ngày trước ngày cuối của dữ liệu (censoring);
   tách riêng cặp đã mở hết hoặc chỉ có 1 thành tựu. In số dòng mỗi lần lọc.
5. **So sánh 3 nền tảng trong từng nhóm số thành tựu của game** (ví dụ ≤ 20, 21–50, > 50) (D4).
6. **Độ bất định:** bootstrap **theo người chơi** bằng NumPy: gom tổng theo người trước, rồi lấy mẫu lại danh sách người (D5).
7. **Độ vững:** đổi mốc N (7 / 90 ngày); loại cặp mở hàng loạt (D6). Tuỳ chọn: bảng cohort theo quý bắt đầu (D2).

**Biểu đồ gợi ý (≥ 2):** đường tỉ lệ quay lại theo số ngày kể từ thành tựu đầu của 3 nền tảng · cột tỉ lệ quay lại sau 30
ngày theo nhóm số thành tựu × nền tảng, kèm khoảng tin cậy.

**Rủi ro và cách xử lý:**
- "Không quay lại" không chắc là "bỏ game" (đã chơi xong, hoặc game rất ít thành tựu) → tách riêng các nhóm này.
- Cách thiết kế thành tựu khác nhau giữa các nền tảng → so sánh trong cùng nhóm số thành tựu, nêu trong hạn chế.
- Mẫu là người săn thành tựu → không áp dụng cho người chơi phổ thông.

**Giảm tải nếu cần:** chỉ dùng mốc chính N = 30; bỏ phân tích theo thể loại (26% game PS thiếu thông tin thể loại);
bỏ cohort (vẫn còn D1, D3, D4, D5, D6).

**Khác với phân tích đã có:** tác giả đo tỉ lệ hoàn thành (% thành tựu đạt được) và MAU/WAU. Câu này đo việc **quay lại một game
theo thời gian** sau khi bắt đầu. Vẫn phải khai báo trong README vì cùng chủ đề hành vi người chơi.

---

## 6. Q4 — Review nào sẽ được bình chọn "helpful"? (ML)

**Câu hỏi (nháp):** Ngay khi một review Steam vừa được đăng, có dự đoán được review đó sẽ nhận **ít nhất hai** lượt "helpful"
không? Ngoài độ dài, những đặc điểm nào của review, người viết và game quyết định điều đó?

> *English draft:* At the moment a Steam review is posted, can we predict whether it will receive at least two "helpful"
> votes, and beyond its length, which characteristics of the review, its author and the game drive that prediction?

> **Vì sao là "ít nhất hai" (cập nhật 2026-11-21):** script thu thập của tác giả đọc số vote bằng mẫu
> "N people found this review helpful". Steam viết một vote là "1 person", nên review có đúng 1 vote bị ghi thành 0:
> dữ liệu có **0** review `helpful = 1` nhưng 98.268 review `helpful = 2`. Do đó `helpful > 0` thực chất nghĩa là
> **≥ 2 vote**, và nhóm "0" gồm cả review có 0 vote lẫn review có 1 vote. Phải ghi rõ định nghĩa này trong notebook
> (xem notebook 01, mục 1.4, hạn chế 4).

**Người dùng của dự đoán:** Steam (hoặc một trang tổng hợp review) cần xếp hạng review **mới** khi chưa có lượt bình chọn nào,
để người mua đọc được review hữu ích sớm hơn.

**Bằng chứng từ dataset:**
- 1.204.534 review, không trùng `reviewid`; 100% tác giả có trong `players` (thiếu ngày tạo tài khoản 8,7%);
  51 review có ngày đăng **trước** ngày tạo tài khoản → lỗi dữ liệu, loại.
- **Target** `helpful > 0` (= ≥ 2 vote, xem ở trên): **34%** dương → accuracy dễ gây hiểu nhầm (đoán toàn "không" đã đúng 66%).
- **Lỗi do cách thu thập** (đọc từ script của tác giả, kiểm chứng trên dữ liệu):
  - số vote có dấu phẩy hàng nghìn chỉ giữ 3 chữ số cuối ("1,234" → 234, "1,000" → 0), nên `helpful` không bao giờ vượt 999;
    review có đúng 1.000, 2.000… vote bị ghi thành 0 (rất hiếm, không đổi được nhãn của phần lớn dữ liệu);
  - `posted` là ngày **sửa lần cuối** nếu review đã được sửa, nên "thời điểm đăng" có thể muộn hơn thực tế;
  - chỉ có review của game nằm trong CSDL của tác giả, và tác giả review là người chơi lấy bằng snowball qua danh sách bạn bè.
- **Tỉ lệ được vote theo năm đăng:** 2010–2012: 10–17% · 2013–2018: 35–42% · 2019–2024: 29–34% · 2025: 24,5%.
  → trước 2013 khác hẳn (có thể do hệ thống review của Steam khi đó khác); review gần đây chưa đủ thời gian nhận vote.
- **Độ dài:** trung vị 9 từ; 32,7% review ≤ 3 từ. Tỉ lệ được vote tăng từ 23,5% (≤ 3 từ) lên 65,7% (> 100 từ).
- **Độ phổ biến của game, ngược chiều:** review của game ít review được vote 55,7%; game nhiều review nhất chỉ 16,9%.
- **Tuần cuối tháng 11 mỗi năm** (2019–2024) số review tăng gấp 4–5 lần; review tuần đó ngắn hơn (6 so với 9 từ) và
  ít được vote hơn (22,7% so với 36,1%, đo năm 2023).
- **Tác giả lặp lại:** 196.698 tác giả, có người viết 14.893 review; với cách chia ở dưới, 74% tác giả trong tập test cũng có
  trong tập train.
- **Thử nhanh** (train 2014–2020, test 2021–2022, chỉ dùng feature số): baseline AP 0,31 · chỉ dùng độ dài 0,51 ·
  HistGradientBoosting đủ feature 0,66 → mô hình học được nhiều hơn "review dài thì được vote".

**Đủ 6 yêu cầu ML của đề (phiên bản tối giản):**

| Yêu cầu | Kế hoạch |
| --- | --- |
| 1. Bài toán, người dùng, chống leakage | Phân loại nhị phân `helpful > 0` (= ≥ 2 vote) tại thời điểm đăng. **Loại:** `helpful` (chính là target), `funny`, `awards` (bình chọn đến **sau** khi đăng), `purchased_games`, `friends` (ảnh chụp năm 2025), giá game (chỉ có giá 2024–25), tổng số review của game trên cả dataset (chứa thông tin tương lai). |
| 2. Chia dữ liệu | **Theo thời gian** theo `posted`: train 2014–2020, test 2021–2022. Bỏ trước 2014 và từ 2023 (giải thích bằng bảng tỉ lệ theo năm). Báo thêm kết quả trên nhóm **tác giả mới** (không có trong train). |
| 3. ≥ 2 mô hình + baseline, `Pipeline` | Baseline `DummyClassifier`. Mô hình: `LogisticRegression` (với `StandardScaler` trong `Pipeline`), `HistGradientBoostingClassifier` hoặc `RandomForestClassifier`. |
| 4. Tune bằng CV trên train, test một lần, metric có lý do | `GridSearchCV` + `TimeSeriesSplit` trên tập train, lưới tham số nhỏ; metric chính **average precision (PR-AUC)**; chạy tập test đúng một lần. |
| 5. Phân tích lỗi | Theo nhóm độ dài, độ phổ biến của game, năm đăng, tác giả mới / cũ, tuần cuối tháng 11; in vài dòng dự đoán sai. |
| 6. Diễn giải, trả lời câu hỏi | `permutation_importance` trên một mẫu con của tập test; trả lời: ngoài độ dài, đặc điểm nào quyết định. |

**Feature (đều có tại thời điểm đăng, tính bằng pandas và regex):** số từ, số ký tự, có định dạng (`[h1]`, `[b]`, `[list]`,
xuống dòng), ASCII hay không · tuổi tài khoản lúc đăng (`posted − created`) · số ngày từ khi game phát hành ·
số review game đó đã có **trước ngày đăng** · số review tác giả đã viết **trước ngày đăng** · đăng trong tuần cuối tháng 11 hay không.

**Rủi ro và cách xử lý:**
- `posted` chỉ có ngày, không có giờ → feature "đã có trước đó" phải đếm **trước ngày đăng**, không đếm review cùng ngày.
- `posted` có thể là ngày sửa → một số review bị xếp vào năm muộn hơn; không tách được trong dữ liệu, nêu trong hạn chế.
- Nhãn bị ảnh hưởng bởi lỗi đọc số vote → định nghĩa target là "≥ 2 vote" ngay từ đầu; khi phân tích lỗi, nhớ rằng nhóm "0"
  có lẫn review có 1 vote.
- Hiệu ứng thời gian phơi bày → giới hạn khoảng năm như trên; nêu trong hạn chế.
- Tác giả xuất hiện ở cả train và test → báo riêng kết quả trên tác giả mới.
- Permutation importance trên vài trăm nghìn dòng chạy chậm → dùng mẫu con với `random_state=RANDOM_STATE`.

**Giảm tải nếu cần:** không dùng TF-IDF hay xử lý ngôn ngữ; chỉ 2 mô hình; lưới tham số nhỏ. Vẫn đủ 6 yêu cầu.

**Khác với phân tích đã có:** tác giả không phân tích bảng `reviews`.

---

## 7. Các hướng đã thử và lý do không chọn

| Hướng | Kết quả thử trên dữ liệu | Lý do không chọn |
| --- | --- | --- |
| Q2 cũ: cùng một game, console đắt hơn PC bao nhiêu | Khớp tên: Steam & PS 5.591, Steam & Xbox 5.425 game; trung vị tỉ lệ giá = 1,00; 52–58% bằng giá tuyệt đối | Giá console lẫn giá đang sale (Battlefield V $1,99 trên PS, Steam $49,99); 682 cặp PS chênh > 3 lần; khớp nhầm tên ("The Door"); không kiểm tra độ vững được vì chỉ 1.149 game PS có giá ở cả 3 ngày |
| Q4' cũ (ML dự phòng): dự đoán Platinum PS từ 7 ngày đầu | 863.919 cặp, 32,2% đạt Platinum | 55% Platinum đạt được ngay trong 7 ngày đầu → gần như biết trước đáp án; trùng chủ đề tỉ lệ hoàn thành của tác giả |
| Độ trễ phát hành PC → console | Thoạt nhìn giảm từ khoảng 1 năm (2013–2015) xuống gần 0 (2022–2023) | Do dữ liệu bị cắt cụt (game ra PC gần đây chưa kịp lên console); xử lý xong thì tỉ lệ ra cùng tháng ổn định 40–55% |
| Bạn bè có thư viện game giống nhau không (Steam) | Jaccard giữa bạn bè 0,074, gấp khoảng 1,9 lần cặp ngẫu nhiên | Đáp án hiển nhiên |
| Giá theo khu vực (RUB, JPY…) | Game càng đắt thì tỉ lệ RUB/USD càng thấp | Là bảng giá khu vực Valve gợi ý sẵn → hiển nhiên |
| Bắt đầu chơi sớm sau phát hành thì hoàn thành nhiều hơn (PS) | Tỉ lệ Platinum 36,6% (≤ 30 ngày) → 24,1% (> 3 năm), 610.574 cặp | **Dự phòng cho Q3**: so được trong cùng game (D4 tốt), nhưng gần chủ đề tỉ lệ hoàn thành của tác giả |

## 8. Việc tiếp theo

- [ ] Làm xong notebook 01, rồi hai thành viên chọn giữ / sửa / thay từng câu (ghi lý do vào [`DECISIONS.md`](DECISIONS.md)).
- [ ] Chốt người sở hữu từng câu (mục 1.3).
- [ ] Xem tab *Code* của dataset trên Kaggle, đảm bảo không trùng câu hỏi; ghi vào README mục *Related public work*.
- [ ] Trong Phase 2, đo lại các số liệu ở trên trong notebook 01 bằng code của nhóm, đi sâu vào các cột của 4 câu.
- [ ] Người giữ Q4 bắt đầu học scikit-learn (`Pipeline`, `GridSearchCV`, `TimeSeriesSplit`, `permutation_importance`).
- [ ] Viết lại câu hỏi bằng lời của nhóm, cập nhật README (tiếng Anh), notebook 02/03 (mục 1–3) và ma trận trong `PROJECT_PLAN.md`.
