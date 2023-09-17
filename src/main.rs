use rodio::{source::Source, Decoder, OutputStream};
use std::{fs::File, io::BufReader, thread, time};

fn sleep(secs: u64) {
    thread::sleep(time::Duration::from_secs(secs));
}

fn play_sound() {
    // create the outputStream object
    let (_stream, stream_handle) = OutputStream::try_default().unwrap();
    // read the audio file
    let file = BufReader::new(File::open("audio/reminder.mp3").unwrap());
    // create the decoded and ready to output audio
    let source = Decoder::new(file).unwrap().convert_samples();

    // play the audio
    stream_handle
        .play_raw(source)
        .expect("Something went wrong!");

    sleep(3)
}

fn main() {
    loop {
        sleep(1200);

        play_sound();

        sleep(2);

        play_sound();
    }
}
