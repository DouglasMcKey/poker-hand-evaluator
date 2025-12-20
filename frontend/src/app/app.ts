import {Component, OnInit} from '@angular/core';
import {SharedModule} from "./shared/shared-module";
import {FormsModule} from "@angular/forms";

@Component({
    selector: 'app-root',
    imports: [SharedModule, FormsModule],
    templateUrl: './app.html',
    styleUrl: './app.css'
})
export class App implements OnInit {
    masterDeck: any[] = [];
    selectedHand: any[] = [null, null, null, null, null]
    evaluationResult = "";

    ngOnInit() {
        this.generateDeck();
    }

    generateDeck() {
        /**
         * Build a regular deck of cards and push them to the masterDeck,
         * which will be used to create the select options for the form.
         */
        const cardValues = [
            [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10],
            [11, "Jack"], [12, "Queen"], [13, "King"], [14, "Ace"]
        ]

        // The offset helps to distinguish between suites and should aid in
        // determining potential hand rankings later on.
        const suites = [
            {name: "Hearts", offset: 100},
            {name: "Diamonds", offset: 200},
            {name: "Clubs", offset: 300},
            {name: "Spades", offset: 400}
        ]

        let idCounter = 1;
        suites.forEach(suite => {
            cardValues.forEach(card => {
                this.masterDeck.push({
                    id: idCounter++,
                    face_value: card[1],
                    value: suite.offset + (card[0] as number),
                    display: `${card[1]} of ${suite.name}`
                })
            })
        })
    };

    getAvailableCards() {
        /**
         * Returns a filtered deck of cards by filtering the masterDeck and
         * excludes the cards already picked by hand slots.
         */
        return this.masterDeck.filter(card => {
            // Check if card is already selected in any of the other hand slots.
            const isPicked = this.selectedHand.some(selected => selected?.id === card.id);

            // Return cards not picked.
            return !isPicked;
        });
    }

    onsubmit() {
        console.log("Hand to evaluate:", this.selectedHand);
        this.evaluationResult = "Return the result here!";
    }

    resetForm() {
        this.selectedHand = [null, null, null, null, null];
        this.evaluationResult = ""
    }
}
