## On-class
* WebKit features (important)
* Multiple Storyboard
  * prevent merge conflicts
* no swift to be tested
* no animation/accelerometer in coding
* Major Design pattern: 
  * delegation
  * MVC
  * Singleton
  * (notification)
* Objective-C Data Types
  * `BOOL`
  * `ID`
  * `SELECTOR`
* App States
* ARC vs. MRR: memory management
* Understand hw5 very well (code)
  * Pass data/function between controllers: ?? blocks
  * How to save data: ??
* Creating a tableView (code)
  * Delete cells
  * Set delegate
  * completion handler using blocks

## Scene & Segues

* Use blocks for communication between scenes (save or cancel)
* `typedef returntype(^<#block name#>)(<#arguments#>);`
* block properties should always be *copy*
* Two common styles:
  1. Show: left-to-right navigation
  2. Present Modally: full-screen cover
* Use `prepareForSegue:` to connect
  * Set the completion handler: insert new quote into models; have table view reload data; dismiss view controller

## Data Persistence

1. User Default: `NSUserDefaults` using key value (like `NSDictionary`)
2. Save files to the Document folder using plist
3. Use SQLite
4. Use Core Data

*Folder to save*

* Documents
  * Your application stores its data in Documents, with the exception of NSUserDefaults-based preference settings
* Library
  * NSUserDefaults-based preference settings are stored in the Library/Preferences folder
* tmp
  * Place to store temporary files that will not be backed up by iTunes, but your app has to be responsibility for deleting the files


**User Defaults**

* No high performance
* No complex structure
* Not searchable

```objective-c
NSString *const kCurrentIndexKey = @"CurrentIndex";
- (void) save{
    NSUserDefaults *defaults = [NSUserDefaults standardUserDefaults];
    [defaults setObject:[NSNumber numberWithInt:self.currentIndex] forKey:kCurrentIndexKey];
    [defaults synchronize];
}  

- (NSNumber) read {
  NSNumber *readData = [[NSUserDefaults standardUserDefaults] objectForKey:kCurrentIndexKey];
  return readData;
}
```

*Use of const*
1. Prevent mistype
2. Convenience to auto-complete
3. Declare outside of @interface and @implementation


**Inside Document Folder**

* Accept types:
  * Property List (xml)
  * Text Files
  * Archiving Objects -- `NSCoding` protocol

```objective-c
 NSString *documentsDirPath = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES)[0];
 // Create a file name for your file
 NSString *filename = @"flashcards.plist";
 // Generate the full file path
 _filePath = [NSString stringWithFormat:@"%@/%@", documentsDirPath, filename];
      
 NSLog(@"file path %@", _filePath);
        
 NSArray *flashcardsFromDocumentsDir = [[NSArray alloc] initWithContentsOfFile:_filePath];
```

## App life cycle

**App States**
* Not Running
* Inactive (foreground)
* Active (foreground)
* Background
* Suspended

## Memory

**Two Methods of application memory management**
1. Manual retain-release: MRR
2. Automatic Reference Counting: ARC
  * Using reference-count
  * Invoke `dealloc` automatically

### MRR

**Cocoa's Policy**
* You own object you created: `alloc` `new` `copy` `mutableCopy`
* Take ownership by using `retain`
* When no longer need, relinquish it using `release` or `autorelease` (must relinquish object do not own)
* "Parent" object maintain strong reference to "children", "children" have weak reference to "parents"

**Pratical Memory Management**
* Use accessor methods to set property values
* Don't use accessor methods in initalizer and dealloc
* Use weak reference to avoid retain cycles
* Avoid dealloc object while using
* Don't use dealloc to manage scarce resources
* Collections own the objects they contain
* Ownership policy is implemented using retain counts

**Retain Count**
* When create an object, RC (retain count) is 1
* When send a retain message, RC + 1
* When send a release message, RC - 1
* When you send an object a autorelease message, its retain count is decremented by 1 at the end of the current autorelease pool block.
* If RC == 0 -> object dealloc

### ARC

*Insert `retains` and `releases` into code when compile*

## Web View

**WebKit**
* Follow MVC framework
  * View: `WebView`
  * Object: `WebFrameView` and `WebFrame`
* App Transport Security force to connect with web service through HTTPS

Example:

Read a pdf file

```objective-c
- (void)viewDidLoad {
[super viewDidLoad];
NSString *path = [[NSBundle mainBundle] pathForResource:@"HIG" ofType:@"pdf"];
if (path){
NSData *pdfData = [NSData dataWithContentsOfFile:path];
[(UIWebView *)self.view loadData:pdfData MIMEType:@"application/pdf"
textEncodingName:@"utf-8" baseURL:nil];
}
}
```

Read a url

```objective-c
NSURL *url = [NSURL URLWithString:@"https://www.apple.com"];
NSURLRequest *request = [NSURLRequest requestWithURL:url];
[self.myWebView loadRequest: request];
```

Cancel a loading request

```objective-c
- (void)viewWillDisappear:(BOOL)animated{
[super viewWillDisappear:animated];
if ([self.myWebView isLoading]){
[self.myWebView stopLoading];
}
// Disconnect the delegate as the webview is hidden
self.myWebView.delegate = nil;
}
```

Animation loading in WebView

```objective-c
- (void)webViewDidStartLoad:(UIWebView *)webView{
[self.activityIndicator startAnimating];
}
- (void)webViewDidFinishLoad:(UIWebView *)webView{
[self.activityIndicator stopAnimating];
}
- (void)webView:(UIWebView *)webView didFailLoadWithError:(NSError *)error{
[self.activityIndicator stopAnimating];
}
```

*Notes*

1. A web view automatically converts telephone numbers that appear in web content to Phone links.
2. You should not embed `UIWebView` or `UITableView` objects in `UIScrollView` objects.

## Table View Rewind

### Modifying Tables

**Delete table cells**
* Add navigation control
* Enable edit button in `viewDidLoad` method
* Use the public remove method in the model
* Implement `tableView: commitEditingStyle: forRowAtIndexPath` method

```objectiv-c
- (void)tableView:(UITableView *)tableView commitEditingStyle:(UITableViewCellEditingStyle)editingStyle forRowAtIndexPath:(NSIndexPath *)indexPath {
    if (editingStyle == UITableViewCellEditingStyleDelete) {
        // Delete the row from the data source
        [self.model removeFlashcardAtIndex:indexPath.row];
        [tableView deleteRowsAtIndexPaths:@[indexPath] withRowAnimation:UITableViewRowAnimationFade];
    } else if (editingStyle == UITableViewCellEditingStyleInsert) {
        // Create a new instance of the appropriate class, insert it into the array, and add a new row to the table view
    }   
}
```