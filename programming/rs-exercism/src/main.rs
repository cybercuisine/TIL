pub fn annotate(minefield: &[&str]) -> Vec<String> {
    let mut result = vec![];

    for (r, row) in minefield.iter().enumerate() {
        let mut annotated_row = String::new();

        for (c, cell) in row.chars().enumerate() {
            if cell == '*' {
                annotated_row.push('*');
            } else {
                let mine_count = count_surrounding_mines(minefield, r, c);
                if mine_count > 0 {
                    annotated_row.push(char::from_digit(mine_count as u32, 10).unwrap());
                } else {
                    annotated_row.push(' ');
                }
            }
        }

        result.push(annotated_row);
    }
    result
}

fn count_surrounding_mines(minefield: &[&str], row: usize, col: usize) -> usize {
    let mut count = 0;
    let rows = minefield.len();
    let cols = minefield[0].len();

    let directions = vec![
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),         (0, 1),
        (1, -1), (1, 0), (1, 1)
    ];

    for (dr, dc) in directions {
        let nr = row as isize + dr;
        let nc = col as isize + dc;

        if nr >= 0 && nr < rows as isize && nc >= 0 && nc < cols as isize {
            if minefield[nr as usize].chars().nth(nc as usize).unwrap() == '*' {
                count += 1;
            }
        }
    }
    count
}



fn main() {}

fn remove_annotations(board: &[&str]) -> Vec<String> {
    board.iter().map(|r| remove_annotations_in_row(r)).collect()
}
fn remove_annotations_in_row(row: &str) -> String {
    row.as_bytes()
        .iter()
        .map(|&ch| match ch {
            b'*' => '*',
            _ => ' ',
        })
        .collect()
}
fn run_test(test_case: &[&str]) {
    let cleaned = remove_annotations(test_case);
    let cleaned_strs = cleaned.iter().map(|r| &r[..]).collect::<Vec<_>>();
    let expected = test_case.iter().map(|&r| r.to_string()).collect::<Vec<_>>();
    assert_eq!(expected, annotate(&cleaned_strs));
}
#[test]
fn no_rows() {
    #[rustfmt::skip]
    run_test(&[
    ]);
}
#[test]
fn no_columns() {
    #[rustfmt::skip]
    run_test(&[
        "",
    ]);
}
#[test]
fn no_mines() {
    #[rustfmt::skip]
    run_test(&[
        "   ",
        "   ",
        "   ",
    ]);
}
#[test]
fn board_with_only_mines() {
    #[rustfmt::skip]
    run_test(&[
        "***",
        "***",
        "***",
    ]);
}
#[test]
fn mine_surrounded_by_spaces() {
    #[rustfmt::skip]
    run_test(&[
        "111",
        "1*1",
        "111",
    ]);
}
#[test]
fn space_surrounded_by_mines() {
    #[rustfmt::skip]
    run_test(&[
        "***",
        "*8*",
        "***",
    ]);
}
#[test]
fn horizontal_line() {
    #[rustfmt::skip]
    run_test(&[
        "1*2*1",
    ]);
}
#[test]
fn horizontal_line_mines_at_edges() {
    #[rustfmt::skip]
    run_test(&[
        "*1 1*",
    ]);
}
#[test]
fn vertical_line() {
    #[rustfmt::skip]
    run_test(&[
        "1",
        "*",
        "2",
        "*",
        "1",
    ]);
}
#[test]
fn vertical_line_mines_at_edges() {
    #[rustfmt::skip]
    run_test(&[
        "*",
        "1",
        " ",
        "1",
        "*",
    ]);
}
#[test]
fn cross() {
    #[rustfmt::skip]
    run_test(&[
        " 2*2 ",
        "25*52",
        "*****",
        "25*52",
        " 2*2 ",
    ]);
}
#[test]
fn large_board() {
    #[rustfmt::skip]
    run_test(&[
        "1*22*1",
        "12*322",
        " 123*2",
        "112*4*",
        "1*22*2",
        "111111",
    ]);
}
