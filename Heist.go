package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	rand.Seed(time.Now().UnixNano())
	isHeistOn := true

	eludedGuards := rand.Intn(100)
	if eludedGuards >= 5 {
		fmt.Println("Looks like you've managed to make it past the guards. Good job, but remember, this is the first step.")
		fmt.Println("eludedGuards has a value of", eludedGuards) 
	} else {
		isHeistOn = false
		fmt.Println("Plan a better disguise next time?")
		fmt.Println("eludedGuards has a value of", eludedGuards) 
	}

	openedVault := rand.Intn(100)
	if openedVault >= 7 && isHeistOn {
		fmt.Println("Grab and GO!")
		fmt.Println("openedVault has a value of", openedVault) 
	} else if isHeistOn {
		isHeistOn = false
		fmt.Println("Plan a better disguise next time?")
		fmt.Println("openedVault has a value of", openedVault)
	}

	leftSafely := rand.Intn(5)
	if isHeistOn {
		switch leftSafely {
			case 0:
			isHeistOn = false
			fmt.Println("Plan a better disguise next time?")
			fmt.Println("leftSafely is", leftSafely)
			case 1: 
			isHeistOn = false 
			fmt.Println("Turns out vault doors don't open from the inside...")
			fmt.Println("leftSafely is", leftSafely)
			case 2: 
			isHeistOn = false 
			fmt.Println("Soooo Bad...")
			fmt.Println("leftSafely is", leftSafely)
			case 3: 
			isHeistOn = false 
			fmt.Println("Bad...")
			fmt.Println("leftSafely is", leftSafely)
			default: 
			fmt.Println("Start the getaway car!")
			fmt.Println("leftSafely is", leftSafely)
		}
	}

	fmt.Println("Is heist on?", isHeistOn)
  
	if amtStolen := 10000+rand.Intn(1000000); isHeistOn {
		fmt.Println("How much did we stole:", amtStolen)
	}
}
