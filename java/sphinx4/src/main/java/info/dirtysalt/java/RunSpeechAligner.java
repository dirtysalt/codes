package info.dirtysalt.java;

/**
 * Created by dirlt on 6/7/16.
 */

import edu.cmu.sphinx.api.Configuration;
import edu.cmu.sphinx.api.SpeechAligner;
import edu.cmu.sphinx.result.WordResult;

import java.net.URL;
import java.util.ArrayList;
import java.util.List;

public class RunSpeechAligner {

    public static void main(String[] args) throws Exception {

        Configuration configuration = new Configuration();

        configuration.setAcousticModelPath("resource:/edu/cmu/sphinx/models/en-us/en-us");
        configuration.setDictionaryPath("resource:/edu/cmu/sphinx/models/en-us/cmudict-en-us.dict");
        configuration.setLanguageModelPath("resource:/edu/cmu/sphinx/models/en-us/en-us.lm.bin");

        String text = "five things";

        SpeechAligner aligner = new SpeechAligner(configuration.getAcousticModelPath(), configuration.getDictionaryPath(), null);
        URL wavPath = RunSpeechAligner.class.getResource("/test.wav");
        System.out.println("wavPath = " + wavPath);
        List<WordResult> results = aligner.align(wavPath, text);
        System.out.println("possible appearances");
        List<String> stringResults = new ArrayList<String>();
        for (WordResult sr : results) {
            System.out.println("time frame = " + sr.getTimeFrame().toString() +
                    ", score = " + sr.getScore() + ", word = " + sr.getWord().getSpelling());
            stringResults.add(sr.getWord().getSpelling());
        }
    }
}
