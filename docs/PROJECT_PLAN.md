# Kế hoạch thực hiện đồ án — CSC17104 Final Project

> Bản kế hoạch chung của nhóm. Mọi yêu cầu bên dưới lấy từ đề bài
> [`docs/CSC17104_2026_Final_Project.pdf`](CSC17104_2026_Final_Project.pdf) (số mục trong ngoặc là mục của đề).
> Quy trình làm việc (Git, commit, review, dùng AI) nằm ở [`CONTRIBUTING.md`](../CONTRIBUTING.md).
>
> **Cập nhật trạng thái lần cuối: 2026-11-29.** Phase 0–2 xong phần notebook 01 (mục 1–3, cả hai phía; mục 1, phần game
> mục 2 và mục 3 đã rút gọn); còn ghi quyết định vào `DECISIONS.md` và phần README của Phase 1. Phase 3 bắt đầu tiếp theo.

## 1. Mục tiêu

Thực hiện trọn vẹn một quy trình khoa học dữ liệu trên dataset *Gaming Profiles 2025 (Steam, PlayStation, Xbox)*:
thu thập → khám phá → đặt câu hỏi → phân tích → tổng kết → thuyết trình, **tái lập được** và **làm việc nhóm**
bằng các công cụ của môn (Linux CLI, Git & GitHub, Conda, Jupyter, Python, NumPy, pandas, Matplotlib, scikit-learn).

Điểm cá nhân có thể khác điểm nhóm, dựa trên **Q&A** và **Git history** (5). Vì vậy:
mỗi người tự commit phần mình, và phải giải thích được **mọi dòng** trong repo, kể cả phần người kia viết (6).

## 2. Thành viên

| Ký hiệu | Họ tên | MSSV | GitHub |
| --- | --- | --- | --- |
| A | TODO | TODO | `minhnguyen1210` |
| B | TODO | TODO | `CaoThien1402` |

## 3. Tổng quan các phase

| Phase | Nội dung | Mục đề | Người chính | Sản phẩm | Hạn |
| --- | --- | --- | --- | --- | --- |
| 0 | Setup repo, môi trường, dữ liệu | 4 | A (B review) | repo chạy được trên cả 2 máy | TODO |
| 1 | Thu thập dữ liệu (mô tả nguồn) | 3.1 | A + B | notebook 01 – mục 1 | TODO |
| 2 | Khám phá dữ liệu | 3.2 | A: phía game · B: phía người chơi | notebook 01 – mục 2, 3 | TODO |
| 3 | Đặt câu hỏi (sau khi xong notebook 01) | 3.3 | A + B | bảng câu hỏi trong README | TODO |
| 4 | Phân tích (4 câu) | 3.4 | mỗi người 2 câu | notebook 02_q1–q3, 03 | TODO |
| 5 | Tổng kết & reflection | 3.5 | A + B | notebook 04, README | TODO |
| 6 | Slides & tập thuyết trình | 5 | A + B | `slides.pdf` | TODO |
| 7 | Kiểm tra cuối & nộp | 4 | A + B | repo hoàn chỉnh | TODO |

Phase 2–4 có tính lặp: hiểu dữ liệu hơn thì quay lại sửa phase trước (3).

## 4. Phân công câu hỏi (chọn ở Phase 3, sau khi xong notebook 01)

Nhóm 2 người → **4 câu hỏi**, mỗi người sở hữu đúng 2 câu, **ít nhất 1 câu ML** (3.3).
Các câu ứng viên và bằng chứng (chưa chốt): [`QUESTIONS.md`](QUESTIONS.md).

| Câu | Loại | Notebook | Người sở hữu |
| --- | --- | --- | --- |
| Q1 | non-ML | `02_analysis_q1.ipynb` | TODO |
| Q2 | non-ML | `02_analysis_q2.ipynb` | TODO |
| Q3 | non-ML | `02_analysis_q3.ipynb` | TODO |
| Q4 | ML | `03_ml_question.ipynb` | TODO |

Gợi ý cân bằng khối lượng: câu ML nặng nhất, nên người giữ Q4 giữ thêm 1 câu non-ML;
người còn lại giữ 2 câu non-ML.

**Ma trận tiêu chí độ sâu** (điền ở Phase 3, kiểm tra lại ở Phase 7): mỗi câu non-ML ≥ 2 tiêu chí,
cả 3 câu non-ML gộp lại ≥ 4/6 tiêu chí.

| | D1 Ghép dữ liệu | D2 Reshape & thời gian | D3 Biến phái sinh | D4 Kiểm soát nhiễu | D5 Độ bất định | D6 Độ vững |
| --- | --- | --- | --- | --- | --- | --- |
| Q1 | | | | | | |
| Q2 | | | | | | |
| Q3 | | | | | | |
| **Tổng phủ** | | | | | | |

## 5. Chi tiết từng phase

### Phase 0 — Setup (4)

| Việc | Ai | Xong khi | Trạng thái |
| --- | --- | --- | --- |
| Cấu trúc repo đúng mục 4 của đề | A | có đủ `README.md`, `environment.yml`, `LLM_USAGE.md`, `data/`, `src/`, `notebooks/` | ✅ |
| `environment.yml` tái lập được | A | `conda env create -f environment.yml` chạy được trên máy A và B | ✅ (B chạy notebook 01 bằng kernel `gaming-ds` trong PR #1) |
| Script tải dữ liệu | A | `bash scripts/download_data.sh` đưa đủ 21 file (phiên bản 1) vào `data/raw/<platform>/` | ✅ |
| `.gitignore` chặn dữ liệu | A | `git status` không bao giờ hiện file trong `data/raw/` | ✅ |
| Quy trình nhóm: `CONTRIBUTING.md`, kế hoạch, nhật ký quyết định, template PR/issue, hook chặn AI | A | cả hai đã đọc và đồng ý | ⏳ B đã làm theo quy trình PR (PR #1, #4) nhưng chưa xác nhận `DECISIONS.md` #1–5 |
| Commit đầu tiên + push | A | `main` trên GitHub có commit `setup: ...` | ✅ |
| Bảo vệ nhánh `main` trên GitHub | A | làm theo `CONTRIBUTING.md` mục 8 | ⏳ (2026-11-29: `main` vẫn chưa có ruleset hay branch protection) |
| B chấp nhận lời mời repo, clone, setup theo `CONTRIBUTING.md` mục 3 | B | B chạy ô setup của notebook 01 không lỗi | ✅ (PR #1) |
| Điền tên, MSSV vào README và mục 2 của file này | A, B | không còn TODO ở bảng thành viên | ⏳ |

### Phase 1 — Thu thập dữ liệu (3.1) → notebook 01, mục 1

Trả lời **bằng lời của nhóm** trong notebook:

Trạng thái: notebook 01 mục 1.1–1.5 xong (A, PR #2, merge 2026-11-23; rút gọn 2026-11-28: bỏ hình ERD và hạn chế #9,
giữ nguyên số thứ tự hạn chế 1–8); còn phần README.

- [x] **Subject:** dữ liệu nói về gì, bối cảnh thực tế nào. (mục 1.1)
- [x] **Source:** nền tảng, URL đầy đủ, tác giả/tổ chức, ngày công bố. (mục 1.2)
- [x] **License:** loại license, ràng buộc, yêu cầu ghi công. (mục 1.3)
- [x] **Collection method:** cách thu thập, tổng thể nào, giai đoạn nào, hạn chế và thiên lệch đã biết. (mục 1.4)
- [x] **Motivation:** vì sao nhóm chọn dataset này. (mục 1.5)
- [ ] README: điền mô tả dataset, mục "known limitations", và **liệt kê các notebook công khai liên quan**
      (tab *Code* trên Kaggle + 2 notebook của tác giả) kèm **câu hỏi của nhóm khác ở đâu** (2).
      ⏳ Đã có mô tả dataset và 2 notebook của tác giả (dòng `private_steamids` sửa 2026-11-29); còn TODO: known
      limitations, notebook Kaggle, "how we differ".

### Phase 2 — Khám phá dữ liệu (3.2) → notebook 01, mục 2–3

Nguyên tắc của đề: **đi sâu vào cột liên quan tới câu hỏi**, các cột khác tóm tắt ngắn, **không vẽ mỗi cột một biểu đồ**.

Chia theo nhóm bảng để làm song song (mỗi người viết phần bảng của mình trong notebook 01; [`DECISIONS.md`](DECISIONS.md) #6):

| Nhóm bảng | Bảng | Người | Đã xong |
| --- | --- | --- | --- |
| Phía game | `games`, `achievements`, `prices` (3 nền tảng) | A | ✅ mục 2.1–2.8 + các ý phía game ở mục 3 (PR #3, merge 2026-11-23; rút gọn và tối ưu code 2026-11-28/29) |
| Phía người chơi | `players`, `history`, `purchased_games` (3 nền tảng); `reviews`, `friends`, `private_steamids` (Steam) | B | ✅ mục 2.1–2.8 (PR #1, #4) + các ý phía người chơi ở mục 3 (PR #5, merge 2026-11-26) |

Checklist cho mỗi bảng được dùng (cả hai phía đã xong):

- [x] **Loading strategy:** bảng nào đọc toàn bộ, bảng nào đọc theo chunk / `usecols` / `dtype` (bảng `history` 600–800 MB mỗi nền tảng).
- [x] **Overview:** số dòng, số cột; một dòng là gì; ý nghĩa và kiểu từng cột; cột cần bỏ/đổi kiểu; dòng trùng/rỗng và có xoá không (giải thích).
- [x] **Cột số:** phân phối, trung tâm, độ phân tán; min/max hợp lý không; outlier (IQR, z-score) thật hay lỗi; giá trị giữ chỗ.
- [x] **Cột phân loại:** số giá trị khác nhau, phổ biến nhất; cân bằng; nhãn không thống nhất/lỗi chính tả; nhóm hiếm cần gộp.
- [x] **Thiếu dữ liệu:** số lượng và % mỗi cột; có quy luật không; vì sao thiếu; xử lý thế nào (bỏ / điền / nhóm riêng).
- [x] **Quan hệ:** tương quan biến số; bảng chéo, thống kê theo nhóm; quan hệ bất ngờ.

Làm chung ở cuối notebook 01:

- [x] **Tóm tắt khám phá:** 3–5 quan sát chính; vấn đề chất lượng nghiêm trọng; **kế hoạch tiền xử lý**; pattern có thể thành câu hỏi.
      (mục 3.1–3.4, cả hai phía)
- [x] Hàm đọc/làm sạch dùng lại nhiều lần → đưa vào `src/` (có docstring), không copy-paste giữa các notebook.
      (`load_game_table`, `parse_list_column`, `load_player_table`, `count_list_items`, `parse_id_list`, `report_rows`)

Việc còn lại để đóng Phase 2 (rà soát notebook 01 ngày 2026-11-26, cập nhật 2026-11-29):

- [x] Ô đầu notebook: điền **Inputs** và **Outputs**. (B, PR #5)
- [x] Mục 3.1–3.4: thêm các ý phía người chơi. (B, PR #5)
- [x] Mục 2.8 phía người chơi: "384 reviews posted before the account was created" bị đếm thừa vì `posted` chỉ có ngày
      (00:00) còn `created` có giờ; so theo ngày thì chỉ có **51** review. Đã sửa code và câu nhận xét (A sửa thay B
      ngày 2026-11-29, B xem lại trong PR); câu giải thích cũ "probably edited" cũng sai (sửa review làm ngày muộn hơn,
      không sớm hơn) nên đã bỏ.
- [x] Đoạn mở đầu mục 2.4–2.8 chỉ mô tả phía người chơi; đã thêm phía game. (A, 2026-11-28)
- [x] Mục 2.1: số giây đọc file trong chữ lệch với output; đã viết lại theo khoảng gần đúng. (A, 2026-11-28/29)
- [ ] Commit bản notebook 01 chạy lại từ kernel sạch (Restart & Run All, thứ tự ô 1→28). (A, PR tiếp theo)
- [ ] Ghi các quyết định trong notebook 01 vào [`DECISIONS.md`](DECISIONS.md): loại playtest; gộp nhãn genre khác hoa
      thường, nhãn < 1 % thành "Other"; so genre trong từng nền tảng; ngày 22/02/2025 làm ngày so giá; giá 0 coi là thiếu;
      `country` < 1 % thành "Other", thiếu thành "Unknown"; đơn vị phân tích hành vi là cặp (người chơi, game);
      `games` chỉ left join khi cần thuộc tính.

### Phase 3 — Đặt câu hỏi (3.3) → README + đầu mỗi notebook 02/03

- [ ] Đọc bộ câu đề xuất và bằng chứng trong [`QUESTIONS.md`](QUESTIONS.md); mỗi người có thể đề xuất thêm câu ứng viên dựa trên tóm tắt khám phá.
- [ ] Loại câu "không đạt": trả lời được bằng 1 `groupby`/`value_counts`/`describe` + 1 biểu đồ; chỉ mô tả 1 biến; đáp án hiển nhiên.
- [ ] Đối chiếu với các notebook công khai: **không trùng** câu hỏi của tác giả / Kaggle.
- [ ] Chốt 4 câu, mỗi câu có: **câu hỏi** (đủ cụ thể để trả lời bằng dữ liệu), **động lực** (ai quan tâm, giúp quyết định gì), **người sở hữu**.
- [ ] Điền ma trận D1–D6 ở mục 4 của file này; đạt ≥ 2/câu và ≥ 4/6 tổng.
- [ ] Với câu ML: xác định trước người dùng của dự đoán, thời điểm dự đoán, cột bị loại (leakage), cách chia train/test.
- [ ] Cập nhật bảng Questions và Question ownership trong README.

### Phase 4 — Phân tích (3.4) → mỗi người làm notebook của mình

**Mỗi câu non-ML (02_analysis_qN):**

- [ ] Tiền xử lý: mô tả các bước bằng Markdown trước, rồi mới code.
- [ ] **In số dòng sau mỗi bước làm thay đổi dữ liệu** (lọc, merge, xoá) và giải thích thay đổi.
- [ ] Nếu merge (D1): báo số dòng trước/sau và số key không khớp.
- [ ] Phương pháp: nói rõ dùng gì và vì sao phù hợp.
- [ ] Dùng rõ ràng ≥ 2 tiêu chí D1–D6 (ghi vào bảng tiêu chí trong notebook).
- [ ] **≥ 2 biểu đồ** có tiêu đề, nhãn trục, đơn vị, chú thích.
- [ ] **Trả lời câu hỏi bằng con số cụ thể.**
- [ ] Thảo luận: ý nghĩa thực tế, điều bất ngờ, hạn chế.

**Câu ML (03_ml_question) — đủ 6 yêu cầu của đề:**

- [ ] Bài toán dự đoán có người dùng rõ ràng; chỉ dùng feature có tại thời điểm dự đoán; **liệt kê cột bị loại vì leakage**.
- [ ] Chia dữ liệu đúng: theo thời gian (dữ liệu có thời gian) hoặc theo nhóm (nhiều dòng cùng một người chơi/game).
- [ ] ≥ 2 mô hình + 1 baseline đơn giản; **mọi tiền xử lý nằm trong `Pipeline`**.
- [ ] Tune bằng cross-validation **chỉ trên train**; test **đúng 1 lần**; metric có giải thích.
- [ ] Phân tích lỗi: sai ở nhóm con nào, khoảng giá trị nào, ví dụ dòng cụ thể.
- [ ] Diễn giải (ví dụ permutation importance) và **trả lời câu hỏi gốc**, không chỉ báo điểm.
- [ ] Đặt `random_state` cố định để kết quả tái lập.

**Review chéo:** người kia review PR của từng câu theo checklist trong `CONTRIBUTING.md`, và phải hiểu được code
(vì Q&A có thể hỏi bất kỳ ai về bất kỳ phần nào).

### Phase 5 — Tổng kết & reflection (3.5) → notebook 04 + README

- [ ] **Key findings:** 3–5 phát hiện quan trọng nhất, nêu bật phát hiện bất ngờ nhất (làm chung).
- [ ] **Hạn chế:** của dữ liệu, phương pháp, phạm vi (làm chung).
- [ ] **Hướng phát triển:** câu hỏi, dữ liệu, phương pháp sẽ thêm (làm chung).
- [ ] **Reflection cá nhân:** mỗi người **tự viết** phần của mình — khó khăn và cách vượt qua, học được gì, dùng LLM thế nào.
      Không dùng AI để viết phần này (6).
- [ ] README: điền tóm tắt dự án và mục Key findings.

### Phase 6 — Slides & thuyết trình (5)

- [ ] Khung slides: mở đầu (dataset, câu hỏi) → mỗi câu hỏi → kết luận. Thời lượng **15 phút** + **10 phút Q&A**.
- [ ] Kể "câu chuyện dữ liệu": câu hỏi, phát hiện, **vì sao biết là đúng**; không đọc code từng dòng.
- [ ] **Mỗi người trình bày 2 câu mình sở hữu.**
- [ ] Xuất `slides.pdf` ở thư mục gốc repo.
- [ ] Tập ít nhất 2 lần có bấm giờ.
- [ ] Chuẩn bị Q&A: mỗi người đọc và tự giải thích được notebook của người kia, `src/`, `environment.yml`, script tải dữ liệu.

### Phase 7 — Kiểm tra cuối & nộp (4)

- [ ] Tạo môi trường mới từ đầu (`conda env create -f environment.yml`) và chạy **toàn bộ notebook theo thứ tự** không lỗi.
- [ ] README đủ 6 nội dung bắt buộc: thành viên + MSSV; phân công; dataset + nguồn + license + notebook công khai liên quan; danh sách câu hỏi; key findings; cách chạy.
- [ ] `LLM_USAGE.md` ghi đủ mọi lần dùng LLM đáng kể (công cụ, hỏi gì, dùng/sửa thế nào).
- [ ] Không có file dữ liệu nào trong repo; không còn `TODO` nào trong README và notebook.
- [ ] Ma trận D1–D6 đạt yêu cầu; mỗi câu có ≥ 2 biểu đồ và câu trả lời có con số.
- [ ] Git history: cả hai người đều có commit cho phần mình; không có commit nào của AI.
- [ ] `slides.pdf` có trong repo.

## 6. Đối chiếu yêu cầu đề → vị trí trong repo

| Yêu cầu (mục đề) | Ở đâu | Trạng thái |
| --- | --- | --- |
| Dataset thật, công khai, ≥ 3.000 dòng, ≥ 10 cột, có license (2) | README – Dataset | ✅ |
| Khai báo phân tích đã có + khác biệt (2) | README – Related public work | ⏳ thiếu notebook Kaggle + "how we differ" |
| Thu thập dữ liệu (3.1) | notebook 01 – mục 1 | ✅ (PR #2, rút gọn 2026-11-28) |
| Khám phá dữ liệu + tóm tắt (3.2) | notebook 01 – mục 2, 3 | ✅ cả hai phía (chờ merge bản chạy lại 2026-11-29) |
| 4 câu hỏi, chủ sở hữu, động lực (3.3) | README – Questions; notebook 02/03 – mục 1, 2 | ⏳ |
| Độ sâu D1–D6 (3.3) | notebook 02 – mục 3; ma trận ở file này | ⏳ |
| Yêu cầu câu ML (3.3) | notebook 03 | ⏳ |
| Phân tích từng câu (3.4) | notebook 02_q1–q3, 03 | ⏳ |
| Tổng kết & reflection (3.5) | notebook 04 | ⏳ |
| Cấu trúc repo (4) | toàn repo | ✅ |
| README đủ nội dung (4) | README | ⏳ |
| `slides.pdf` (4) | thư mục gốc | ⏳ |
| Ghi nhận dùng LLM (6) | `LLM_USAGE.md` | ⏳ |
