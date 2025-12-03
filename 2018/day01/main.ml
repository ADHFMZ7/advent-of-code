let file = "input"

let () =
 let ic = open_in file in
  try
    let line = input_line ic in
    (* read line, discard \n *)
    print_endline line;
    (* write the result to stdout *)
    flush stdout;
    (* write on the underlying device now *)
    close_in ic
    (* close the input channel *)
  with e ->
    (* some unexpected exception occurs *)
    close_in_noerr ic;
    (* emergency closing *)
    raise e


