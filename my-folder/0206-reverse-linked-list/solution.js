/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
    if (!head)
        return null

    const arr = []
    let tmp_list = head

    while(tmp_list){
        arr.push(tmp_list)
        tmp_list = tmp_list.next

    }
    for (let i = arr.length -1 ; i > 0; i--){
        arr[i].next = arr[i-1]
    }

    arr[0].next = null
    return arr[arr.length -1]
};
