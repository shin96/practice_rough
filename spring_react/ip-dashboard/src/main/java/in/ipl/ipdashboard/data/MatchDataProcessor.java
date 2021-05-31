package in.ipl.ipdashboard.data;

import java.time.LocalDate;

// import org.slf4j.Logger;
import org.springframework.batch.item.ItemProcessor;

import in.ipl.ipdashboard.model.Match;

public class MatchDataProcessor implements ItemProcessor<MatchInput, Match> {

    // private static final Logger log = org.slf4j.LoggerFactory.getLogger(MatchDataProcessor.class);

    @Override
    public Match process(final MatchInput matchInput) throws Exception {
        Match match = new Match();
        match.setId(Long.parseLong(matchInput.getId()));
        match.setCity(matchInput.getCity());
        match.setDate(LocalDate.parse(matchInput.getDate()));
        match.setMatchWinner(matchInput.getWinner());
        match.setPlayerOfMatch(matchInput.getPlayer_of_match());
        match.setResult(matchInput.getResult());
        match.setResultMargin(matchInput.getResult_margin());

        // Set team 1 and team 2 depending on the inngings order
        String firstInningsTeam;

        String secondInningsTeam;
        if ("bat".equals(matchInput.getToss_decision())) {
            firstInningsTeam = matchInput.getToss_winner();
            secondInningsTeam = matchInput.getToss_winner().equals(matchInput.getTeam1()) 
                ? matchInput.getTeam2() : matchInput.getTeam1();

        } else {
            secondInningsTeam = matchInput.getToss_winner();
            firstInningsTeam = matchInput.getToss_winner().equals(matchInput.getTeam1()) 
                ? matchInput.getTeam2() : matchInput.getTeam1();
        }
        match.setTeam1(firstInningsTeam);
        match.setTeam2(secondInningsTeam);

        match.setTossDecision(matchInput.getToss_decision());
        match.setTossWinner(matchInput.getToss_winner());
        match.setVenue(matchInput.getVenue());
        match.setUmpire1(matchInput.getUmpire1());
        match.setUmpire2(matchInput.getUmpire2());

        return match;

    }
}