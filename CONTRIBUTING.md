# Quy trình làm việc của nhóm

> Thoả thuận chung giữa hai thành viên. Ai cũng phải đọc và làm theo trước khi commit lần đầu.
> Kế hoạch theo phase: [`docs/PROJECT_PLAN.md`](docs/PROJECT_PLAN.md).
> Nhật ký quyết định chung: [`docs/DECISIONS.md`](docs/DECISIONS.md).
> Muốn đổi quy tắc nào thì sửa file này qua một Pull Request và cả hai cùng đồng ý.

## 1. Nguyên tắc bắt buộc

1. **AI không bao giờ thao tác Git thay người.** Claude, ChatGPT, Copilot… không được chạy `git commit`, `git push`,
   `git merge`, không được tạo hay merge Pull Request. Mọi commit và push do **chính thành viên** gõ lệnh.
2. **Không có dấu vết AI trong Git history.** Không commit nào có tác giả là AI, không có dòng
   `Co-Authored-By: Claude …` hay "Generated with Claude Code". AI không được xuất hiện trong danh sách contributor.
   Có hai lớp chặn, mỗi người phải bật: cấu hình Claude Code trên máy mình (mục 3.2) và hook trong repo (mục 3.3).
3. **AI chỉ là gia sư** (đề, mục 6): được hỏi để hiểu khái niệm, thông báo lỗi, thư viện. **Không** dùng AI để viết phần
   phân tích, câu trả lời, kết luận hay reflection. Mỗi lần dùng đáng kể phải ghi vào [`LLM_USAGE.md`](LLM_USAGE.md):
   ngày, người, công cụ, đã hỏi gì, đã dùng hoặc sửa câu trả lời thế nào.
4. **Giải thích được mọi dòng.** Không commit thứ mình không hiểu. Phần không giải thích được trong Q&A bị coi là không
   phải của mình.
5. **Không commit dữ liệu.** Không đưa file nào trong `data/raw/`, `data/processed/`, hay bất kỳ `.csv`, `.parquet`,
   `.zip`… vào Git.
6. **Không force-push, không push thẳng vào `main`.** Mọi thay đổi vào `main` đi qua Pull Request được người kia duyệt.
7. **Không tự ý sửa phần của người kia** (notebook câu hỏi của người kia, đoạn trong notebook 01 người kia phụ trách)
   khi chưa trao đổi.
8. **Ghi nguồn khi dùng code hay ý tưởng của người khác** (notebook công khai, StackOverflow, tài liệu). Chép không ghi
   nguồn là đạo văn, bị 0 điểm cả đồ án.

## 2. Phân vai

| Vai trò | Người |
| --- | --- |
| Chủ repo (cài đặt GitHub, bảo vệ nhánh `main`) | `minhnguyen1210` |
| Chủ sở hữu từng câu hỏi, từng phần khám phá | xem [`docs/PROJECT_PLAN.md`](docs/PROJECT_PLAN.md), mục 4 và Phase 2 |
| Review | mỗi PR do người **không** viết PR đó duyệt |

## 3. Setup một lần cho mỗi thành viên

### 3.1 Repo, môi trường, dữ liệu

```bash
git clone https://github.com/minhnguyen1210/Gaming-Profiles.git
cd Gaming-Profiles
conda env create -f environment.yml
conda activate gaming-ds
bash scripts/download_data.sh        # không cần tài khoản Kaggle; hoặc tải tay, xem README
```

**Danh tính Git phải khớp tài khoản GitHub**, nếu không commit sẽ không được tính cho bạn:

```bash
git config user.name  "Họ Tên"
git config user.email "email-đã-đăng-ký-trên-GitHub"
```

### 3.2 Tắt dòng co-author của Claude Code

**Claude không bao giờ được xuất hiện trong danh sách contributor của repo.** Repo không chứa cấu hình của Claude Code
(thư mục `.claude/` bị `.gitignore` chặn), nên **mỗi người tự cấu hình trên máy mình**. Nếu dùng Claude Code, thêm
cài đặt sau vào file `~/.claude/settings.json` (Windows: `C:\Users\<tên>\.claude\settings.json`):

```json
{
  "attribution": false
}
```

`includeCoAuthoredBy` là tên cũ của cài đặt này, đã bị khai tử; dùng `attribution`.

### 3.3 Bật hook chặn commit có dấu vết AI

Hook [`.githooks/commit-msg`](.githooks/commit-msg) từ chối mọi commit message có dòng ghi công công cụ AI
(Claude, ChatGPT, Copilot, Gemini…). Commit có đồng tác giả là **người** (`Co-authored-by: CaoThien1402 <…>`) vẫn qua.
Git không tự bật hook sau khi clone, nên mỗi người chạy **một lần**:

```bash
git config core.hooksPath .githooks
```

### 3.4 Bật nbdime để xem diff và merge notebook dễ đọc

```bash
nbdime config-git --enable
```

## 4. Quy trình hằng ngày

```bash
# 1. Cập nhật main
git switch main
git pull

# 2. Tạo nhánh cho đúng một việc
git switch -c q1/price-trends

# 3. Làm việc. Trước khi commit:
#    - notebook: Restart & Run All, chạy hết không lỗi
#    - xem lại thay đổi
git status
git diff

# 4. Commit (quy ước ở mục 5)
git add notebooks/02_analysis_q1.ipynb
git commit -m "q1: compare price changes across platforms"

# 5. Đẩy nhánh lên và mở Pull Request trên GitHub
git push -u origin q1/price-trends
```

Sau khi PR được duyệt: bấm **Create a merge commit** (không dùng *Squash*, để giữ nguyên từng commit và tác giả),
xoá nhánh trên GitHub, rồi về máy chạy `git switch main` và `git pull`.

**Thói quen an toàn:** `git add <file cụ thể>`, hoặc đọc kỹ `git status` trước khi `git add .`.

## 5. Quy ước đặt tên

### 5.1 Commit message

```
<scope>: <tóm tắt ngắn, tiếng Anh, viết thường, động từ nguyên mẫu>

<thân (tuỳ chọn): vì sao thay đổi, quyết định quan trọng>
```

- Dòng đầu tối đa 72 ký tự, không có dấu chấm cuối.
- Mỗi commit là một thay đổi có ý nghĩa. Commit thường xuyên, không dồn cả tuần vào một commit.
- Cấm message mơ hồ: `update`, `fix`, `done`, `abc`, `final`, `final2`.

| Scope | Dùng cho |
| --- | --- |
| `setup` | cấu trúc repo, `.gitignore`, `.gitattributes`, script, hook, template |
| `env` | `environment.yml` |
| `collect` | notebook 01 – thu thập dữ liệu (3.1) |
| `explore` | notebook 01 – khám phá dữ liệu (3.2) |
| `questions` | đặt và chốt câu hỏi (3.3) |
| `q1`, `q2`, `q3` | notebook phân tích câu tương ứng |
| `ml` | notebook câu ML (Q4) |
| `src` | module dùng chung trong `src/` |
| `summary` | notebook 04, key findings |
| `slides` | slides thuyết trình |
| `docs` | README, `LLM_USAGE.md`, các file trong `docs/`, file này |
| `fix` | sửa lỗi không thuộc scope nào ở trên |

Ví dụ:

```
explore: profile missing values in history tables
q2: add bootstrap confidence intervals for completion rate
ml: compare logistic regression and random forest with group k-fold
docs: log LLM usage for pandas chunked reading
```

### 5.2 Tên nhánh

`<scope>/<mô-tả-ngắn>`, chữ thường, nối bằng gạch ngang. Ví dụ: `explore/history-tables`, `q1/price-trends`,
`ml/baseline-models`, `docs/readme-team`.

## 6. Quy tắc cho notebook và code

- **Không sửa ô setup** ở đầu notebook (ô tìm thư mục gốc repo và import). Đường dẫn luôn lấy từ `src/config.py`,
  **không** dùng đường dẫn tuyệt đối kiểu `C:\Users\...`.
- **In số dòng sau mỗi bước làm thay đổi dữ liệu** (lọc, merge, xoá) và giải thích thay đổi (đề, mục 3.4).
  Dùng chung hàm `report_rows` trong `src/utils.py` để cả hai in cùng một định dạng, ví dụ
  `df = report_rows(df[df["usd"].notna()], "drop rows without a USD price", len(df))`.
  Khi merge: in số dòng trước, sau, và số key không khớp.
- **Ô Inputs / Outputs ở đầu mỗi notebook:** ghi rõ notebook đọc file nào và ghi ra file nào trong `data/processed/`,
  để người kia và người chấm biết thứ tự chạy.
- **Biểu đồ:** có tiêu đề, nhãn trục, đơn vị, chú thích. Biểu đồ dùng cho README hoặc slides lưu vào
  `reports/figures/` với tên `<scope>_<mô-tả>.png`, ví dụ `q1_price_by_platform.png`.
- **Tái lập:** mọi thứ có yếu tố ngẫu nhiên dùng `random_state=RANDOM_STATE` (= 42, khai báo trong `src/config.py`).
- **Giữ output khi commit** để người chấm đọc được kết quả trên GitHub, nhưng không in cả bảng lớn (dùng `.head()`).
- **Trước khi commit:** *Restart & Run All*, chạy hết từ trên xuống không lỗi.
- **Bảng trung gian** tạo bằng code và lưu vào `data/processed/` (không commit); notebook sau đọc lại từ đó.
- **Hàm dùng nhiều lần** đưa vào `src/` kèm docstring. Thay đổi trong `src/` ảnh hưởng cả hai người nên luôn đi qua PR.
- **Quyết định dùng chung** (quy tắc làm sạch, ngưỡng outlier, khoảng thời gian, cách gộp nhóm…) ghi vào
  [`docs/DECISIONS.md`](docs/DECISIONS.md) để hai người làm nhất quán.
- **Thư viện mới:** thêm vào `environment.yml` (ghi rõ phiên bản), chạy `conda env update -f environment.yml --prune`,
  commit với scope `env`, báo người kia cập nhật. Không `pip install` hay `conda install` lẻ mà không ghi vào file.
- **Notebook dùng chung (01):** mỗi người chỉ sửa phần mình phụ trách; luôn `git pull` trước khi làm;
  mở PR sớm và nhỏ để tránh xung đột.

## 7. Pull Request

Khi mở PR, GitHub tự điền checklist từ [`.github/pull_request_template.md`](.github/pull_request_template.md).
Tiêu đề PR theo quy ước commit, ví dụ `q1: price trends across platforms`.

- Người mở PR tự đánh dấu checklist trước khi gán người review.
- Người review góp ý bằng comment; người viết tự sửa và push thêm commit lên cùng nhánh.
- Chỉ merge khi người review đã bấm **Approve**.

## 8. Cài đặt GitHub (chủ repo làm một lần)

Settings → Branches → Add branch ruleset (hoặc branch protection rule) cho `main`:

- Require a pull request before merging, yêu cầu 1 approval.
- Block force pushes, không cho xoá nhánh `main`.

## 9. Giao tiếp và theo dõi việc

- Mỗi việc trong [`docs/PROJECT_PLAN.md`](docs/PROJECT_PLAN.md) là một **Issue** trên GitHub (dùng mẫu "Công việc"),
  gán đúng người, gắn vào **Milestone** của phase.
- Họp ngắn mỗi tuần (TODO: ngày, giờ, kênh): xong gì, vướng gì, tuần tới làm gì.
- Bị kẹt quá 1 ngày thì báo ngay cho người kia, không để dồn tới hạn.
