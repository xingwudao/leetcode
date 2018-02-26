/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
 public:
  string tree2str(TreeNode* t) {
    if (0 == t) {
      return string();
    }
    string left_str = tree2str(t->left);
    string right_str = tree2str(t->right);
    ostringstream string_stream;
    if (0 < right_str.size()) {
      string_stream << t->val << "(" << left_str << ")"
                    << "(" << right_str << ")";
    } else if (0 == left_str.size()) {
      string_stream << t->val;
    } else {
      string_stream << t->val << "(" << left_str << ")";
    }
    return string_stream.str();
  }
};
