# Exam review Part 1

## Gesture

1. Tap
2. Double Tap
3. Drag
4. Flick
5. Pinch
6. Spread
7. Press
8. Press and tap

**Add gesture recognizer in code**

Single Tap
```objective-c
// ViewController.m: Single Tap
- (void)viewDidLoad {
[super viewDidLoad];
UITapGestureRecognizer *singleTap = [[UITapGestureRecognizer alloc] initWithTarget:self
action:@selector(singleTapRecognized:)];
/* if double click
doubleTap.numberOfTapsRequired = 2;
*/
[self.view addGestureRecognizer:singleTap];
}

- (void) singleTapRecognized: (UITapGestureRecognizer *) recognizer {
self.msgLabel.text = @"You single tapped me!";
}
```

Single & Double Tap
```objective-c
// double tap
UITapGestureRecognizer *singleTap = [[UITapGestureRecognizer alloc] initWithTarget:self
action:@selector(singleTapRecognized:)];
[self.view addGestureRecognizer: singleTap];
UITapGestureRecognizer *doubleTap = [[UITapGestureRecognizer alloc] initWithTarget:self
action:@selector(doubleTapRecognized:)];
doubleTap.numberOfTapsRequired = 2;
[self.view addGestureRecognizer: doubleTap];
// Only recognize single taps if they're not the first of two
[singleTap requireGestureRecognizerToFail: doubleTap];
```

Swipe: should add left and right separately
```objective-c
UISwipeGestureRecognizer *swipeLeft = [[UISwipeGestureRecognizer alloc] initWithTarget:self
action:@selector(swipeGestureRecognized:)];
swipeLeft.direction = UISwipeGestureRecognizerDirectionLeft;
[self.view addGestureRecognizer:swipeLeft];
UISwipeGestureRecognizer *swipeRight = [[UISwipeGestureRecognizer alloc] initWithTarget:self
action:@selector(swipeGestureRecognized:)];
swipeRight.direction = UISwipeGestureRecognizerDirectionRight;
[self.view addGestureRecognizer:swipeRight];
```

***Selector***
* accept a method name
* not explicit call

## Animation: Core Animation

**View Properties**
* frame (position and size)
* transform
* alpha (transparency)
* color
* background color

**Block properties**
1. can be pass around to methods or functions as if they were values.
2. is OC object, so can be added to collections like NSArray or NSDictionary
3. capture values from enclosing scope
4. used for callback function: code to be exec when finish task

Syntax
```objective-c
^{
NSLog(@"This is a block");
}
```

```objective-c
int multiplier = 7;
int (^myBlock)(int) = ^(int num) { return num * multiplier; }
```

fade-in example
```objective-c
- (void) fadeInStudent:(NSString *) name{
// Alpha = 0 means the text is transparent
self.nameLabel.alpha = 0;
self.nameLabel.text = name;
[UIView animateWithDuration:1.0 animations:^{
// Fade in the text of the label
self.nameLabel.alpha = 1;
}];
}
```

more examples:
```objective-c
// fade in nameLabel
- (void) animateStudent:(NSString *)name{
self.nameLabel.text = name;
[UIView animateWithDuration:1.0 animations:^{
self.nameLabel.alpha = 1;
}];
}

// fade out then fade in
- (void)displayStudent:(NSString *)name{
[UIView animateWithDuration:1.0 animations:^{
// Fade out old text of label
self.nameLabel.alpha = 0;
} completion:^(BOOL finished) {
// Upon completion, call animateStudent
[self animateStudent:name];
}];
}
```

## Accelerometer Gyroscope

**Motion Events**
* move
* shake
* tilt the device

**Some Properties**
1. made up of three accelerometers
2. give measurements in g-forces
  * no movement -- 1g
3. Shake: ***UIEvent***
4. General Orientation: ***UIDevice***
5. Cancel a motion event: An event is canceled if the shake motion is interrupted or if iOS determines that the motion is not valid after all – for example, if the shaking lasts too long. Use ***motionCancelled:withEvent:***

Handle Shake Event
```objective-c
- (BOOL)canBecomeFirstResponder{
return YES;
}
- (void)viewDidAppear:(BOOL)animated{
[super viewDidAppear:animated];
[self becomeFirstResponder];
}
- (void)motionEnded:(UIEventSubtype)motion withEvent:(UIEvent *)event{
if (motion == UIEventSubtypeMotionShake){
NSLog(@"You shook me!");
}
}
```

Responding Changes in Orientation
```objective-c
- (void) viewDidLoad{
// Request to turn on accelerometer and begin receiving accelerometer events
[[UIDevice currentDevice] beginGeneratingDeviceOrientationNotifications];
[[NSNotificationCenter defaultCenter] addObserver:self
selector:@selector(orientationChanged:) name:UIDeviceOrientationDidChangeNotification
object:nil];
}
- (void)orientationChanged: (NSNotification *) notification{
// Respond to changes in device orientation
UIDeviceOrientation currentOrientation = [[UIDevice currentDevice] orientation];
}
- (void)viewDidDisappear:(BOOL)animated{
// Request to stop receiving accelerometer events and turn off accelerometer
[[NSNotificationCenter defaultCenter] removeObserver:self];
[[UIDevice currentDevice] endGeneratingDeviceOrientationNotifications];
}
```

**CMMotionManager obtain data**
* Pull: An app requests that updates start and then periodically
samples the most recent measurement of motion data.
* Push: An app specifies an update interval and implements a block for
handling the data. Then, it requests that updates start, and passes
Core Motion an operation queue and the block. Core Motion delivers
each update to the block, which executes as a task in the operation
queue.

* Pull is the recommended approach for most apps, especially
games. It is generally more efficient and requires less code.
* Push is appropriate for data-collection apps and similar apps that
cannot miss a single sample measurement.

`startDeviceMotionUpdates` – the pull approach
* After you call this method, Core Motion continuously updates the
deviceMotion property of ***CMMotionManager*** with the latest refined
measurements of accelerometer and gyroscope activity, as
encapsulated in a ***CMDeviceMotion*** object.

`startDeviceMotionUpdatesToQueue:withHandler:` – the push approach
* Before you call this method, assign an update interval to the
***deviceMotionUpdateInterval*** property, create an instance of ***NSOperationQueue***, and implement a block of the ***CMDeviceMotionHandler*** type that handles the accelerometer
updates.
* Then, call the `startDeviceMotionUpdatesToQueue: withHandler:` method on the motion-manager object, passing in
the operation queue and the block.

## Audio

**File Formats (audio container) and Data Format (audio encoding)**
* AAC, HE-AAC, AMR, ALAC, iLBC, iMA4...: df
* If space is not an issue, just encode everything with linear PCM.
  * Not only is this the fastest way for your audio to play, but you can play multiple sounds simultaneously without running into any CPU resource issues.
* If space is an issue, most likely you’ll want to use AAC encoding for your background music and IMA4 encoding for your sound
effects.

**Bit Rate**
* When you lower the bytes per second, you lose quality as well.
* If your file is mostly speech, you can probably get
away with a lower bit rate.

**Sample Rates**
* usually 44,100Hz, because it's the same for CD audio.

**Audio Session**
* Playback is enabled and recording is disabled.
  – When the user moves the Silent switch (or Ring/Silent switch on iPhone) to the “silent” position, your audio is silenced.
  – When the user presses the Sleep/Wake button to lock the screen, or when the Auto-Lock period expires, your audio is silenced.
  – When your audio starts, other audio on the device – such as iPod audio that was already playing – is silenced.

**System Sound Service**
* System Sound Services is intended for user-interface sound effects and user alerts
  – It is not intended for sound effects in games
* Alert sounds work best when kept short
  – According to Apple, preferably 2 seconds or less

**AVAudioPlayer**
* Play background music
* Extremely slow: will be a noticeable delay
* If play in bg, check no other sound is playing to prevent two layers of musics going at once
* Phone call will interrupt the music

*Add Audio Framework*
* Add `AudioToolbox.framework` in project targets
* Import



```objective-c
// QuoteViewController.m
#import <AudioToolbox/AudioToolbox.h>
#import "QuoteViewController.h"
@interface QuoteViewController ()
@property (readonly) SystemSoundID soundFileID;
```

**Examples**

Setup for Sound

```objective-c
// QuoteViewController.m
NSString *soundFilePath = [[NSBundle mainBundle] pathForResource:@"Tada" ofType:@"wav"];
NSURL *soundURL = [NSURL fileURLWithPath:soundFilePath];
AudioServicesCreateSystemSoundID((__bridge CFURLRef _Nonnull)(soundURL), &_soundFileID);

// QuoteViewController.m
- (void)singleTapRecognized: (UITapGestureRecognizer *)recognizer{
// Play sound file
AudioServicesPlaySystemSound(self.soundFileID);
[self displayQuote:[self.model randomQuote]];
}

```

Setup for Vibration

```objective-c
// QuoteViewController.m
- (void)doubleTapRecognized: (UITapGestureRecognizer *)recognizer{
// Vibrate
AudioServicesPlaySystemSound(kSystemSoundID_Vibrate);
[self displayQuote:[self.model randomQuote]];
}
```

Create property using **AVFoundation**

```objective-c
// QuoteViewController.m
#import <AVFoundation/AVFoundation.h>
// Other imports…
@interface QuoteViewController ()
@property (strong, nonatomic) AVAudioPlayer *audioPlayer;

// QuoteViewController.m
NSString *path = [NSString stringWithFormat:@"%@/tone.mp3", [[NSBundle mainBundle]
resourcePath]];
NSURL *soundURL = [NSURL fileURLWithPath:path];
NSError *error;
self.audioPlayer = [[AVAudioPlayer alloc] initWithContentsOfURL:soundURL error:&error];
[self.audioPlayer prepareToPlay];

// QuoteViewController.m
- (void)singleTapRecognized: (UITapGestureRecognizer *)recognizer{
// Play audio
[self.audioPlayer play];
[self displayQuote:[self.model randomQuote]];
}
```

## Delegates

**Protocol**
* Is a declaration of a list of methods
* Two kinds of methods: **optional** and **required**

**Delegation**
* Allow for one to one communication between two instances: the **delegate** and **delegator**
  * Delegator: Instance that send events to delegate
  * Delegate: Process events sent from the delegator
  * The delegator is typically a framework object (i.e. textfield, tableview, etc.), and the delegate is typically a custom controller object.

**Three Steps Processes**
1. In your custom class, adopt the delegate's protocol.
2. Implement the appropriate protocol methods.
3. Connect the `delegate` outlet of the delegator (i.e. textfield, tableview, etc.) to your custom class.

**Summary**
* Allowing some objects to be relatively fixed and others highly customized.
* Maximum software reuse and MVC design pattern.

Demo: or but not both

```objective-c
// ViewController.h
@interface ViewController <ProtocolName>
@end

// ViewController.m
@interface ViewController () <ProtocolName>
@end
@implementation ViewController
@end
```

## Table Views

1. iOS can have an unlimited # of rows
2. iOS tables can only be one col wide

**Plain Table View**
* Row seperated into labeled sections and index appears vertically on right (index list)
* Header and footer: row are grouped, doesn't include index
* Highlight:
  * In both styles, a table row becomes highlighted briefly when a user taps a selectable item.
  * If a row selection results in navigation to a new screen, the selected row becomes highlighted briefly as the new screen slides into place.
  * When the user navigates back to the previous screen, the originally selected row again becomes highlighted briefly to remind the user of the earlier selection (it doesn’t remain highlighted).
* **Four Predefined Styles**
  1. `UITableViewCellStyleDefault`: The default cell style includes an optional image in the left end of the row, followed by a left-aligned title.
  2. `UITableViewCellStyleSubtitle`: The subtitle style includes an optional image in the left end `of the row, followed by a left- aligned title on one line and a left- aligned subtitle on the line below.
  3. `UITableViewCellStyleValue1`: The value 1 style displays a left-aligned title with, on the same line, a rightaligned subtitle in a lighter font.
  4. `UITableViewCellStyleValue2`: The value 2 style displays a right-aligned title in a blue font, followed on the same line by a left-aligned subtitle in a black font. Images don’t fit well in this style.

**Reusing Cell**
* When you call `[tableView dequeuereusablecellwithidentifier:]` you either:
    A. Get a cell that has previously been created and isn't currently being used
    OR
    B. Create a new cell of the class you specified

**Examples**

```objective-c
// ExampleTableViewController.m
// Return the number of sections
- (NSInteger)numberOfSectionsInTableView:(UITableView *)tableView{
return 1;
}

// Return number of rows in the section
- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section{
return 100;
}

// Configuring Rows (cell)
- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:
(NSIndexPath *)indexPath{
static NSString *cellIdentifier = @"TableCell";
UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:cellIdentifier];
// Configure the cell
cell.textLabel.text = [NSString stringWithFormat:@"Row %d", indexPath.row];
return cell;
}
```

**Relationships btw View Controllers**
* If the relationship is a *segue*, the destination view controller is instantiated when the segue is triggered.
* If the relationship represents *containment*, the child view controller is instantiated when its parent is instantiated.
* If the controller is not the destination or child of another controller, it is never instantiated automatically. You must instantiate it from the storyboard programmatically.
  * Segues: When a segue is triggered, iOS takes the following actions:
    1. It instantiates the destination view controller
    using the attribute values you provided in the
    storyboard.
    2. It gives the source view controller an opportunity
    to configure the new controller.
    3. It performs the transition configured in the segue.
* Summary: containment for parent-child connection; segues for two views.